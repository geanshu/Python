//对应首页上的座位扫码功能
function seatScan() { 
	// seatMainScan('HNU13F2077');  //测试扫码预约情况
 	wx.scanQRCode({
		needResult: 1, // 当needResult 为 1 时，扫码返回的结果
		scanType: ["qrCode", "barCode"], // 可以指定扫二维码还是一维码，默认二者都有
		desc: 'scanQRCode desc',
		async: false,
		success: function(res) {
			var barcode = res.resultStr;
			//判断是否开启定位
			mui.ajax("/mobile/ajax/seat/SeatCheckHandler.ashx", {
				data: {
					data_type: 'checkPositionIsEnable',
					barcode: barcode
				},
				async: false,
				dataType: 'json', // 服务器返回json格式数据
				type: 'post', //HTTP请求类型
				timeout: 10000, //超时时间设置为10秒
				success: function(result) {
					//如果开启了定位功能
					if (result.code == 0) {
						//获取定位信息
						wx.getLocation({
							type: 'wgs84', // 默认为wgs84的gps坐标
							success: function(res) {								
								var latitude = res.latitude; // 纬度，浮点数，范围为90 ~ -90
								var longitude = res.longitude; // 经度，浮点数，范围为180 ~ -180。
								var speed = res.speed; // 速度，以米/每秒计
								var accuracy = res.accuracy; // 位置精度	

								//判断是否在馆内进行座位扫码
								seatScanCheckPostion(barcode, latitude, longitude);
							},
							fail: function(res) {
								mui.alert("地理位置获取失败，请将微信的位置信息权限设置为允许！");
								mui.back();
							}
						});
					} else if (result.code == 1) {
					 	seatMainScan(barcode);
					} else {
						mui.toast(result.msg);
					}
				},
				error: function(xhr, type, errorThrown) {
					mui.toast("操作失败，checkPositionIsEnable异常");
				}
			});
		},
		error: function(xhr, type, errorThrown) {
			checklogin(xhr.responseText);
			mui.toast("操作失败，seatScan异常");
		}
	}); 
 }

//对应首页上的座位扫码功能,主要针对师大的APP
function sdappScan(info) {
    var barcode = info["QrCodeInfo"];  

    seatMainScan(barcode);

}

//判断是否在馆内进行座位扫码
function seatScanCheckPostion(barcode, latitude, longitude) {
	mui.ajax("/mobile/ajax/seat/SeatCheckHandler.ashx", {
		data: {
			data_type: 'checkPostion',
			barcode: barcode,
			latitude: latitude,
			longitude: longitude
		},
		async: false,
		dataType: 'json', // 服务器返回json格式数据
		type: 'post', //HTTP请求类型
		timeout: 10000, //超时时间设置为10秒
		success: function(result) {
			if (result.code == 0) {
				seatMainScan(barcode);
			} else {
				mui.toast(result.msg);
			}
		},
		error: function(xhr, type, errorThrown) {
			mui.toast("操作失败，checkPostion异常");
		}
	});
}

//座位扫码处理，判断是扫码落座还是签到签退
function seatMainScan(barCode) {
	mui.ajax("/mobile/ajax/seat/ScanHandler.ashx", {
		data: {
			barcode: barCode,
			data_type: 'seatScan'
		},
		dataType: 'json', //服务器返回json格式数据
		async: false,
		type: 'post', //HTTP请求类型
		timeout: 10000, //超时时间设置为10秒
		success: function(result) {
			if (result.code == 0) {
				//设置扫码座位信息
				setSelectSeatInfo(barCode);
			} else if (result.code == 1) {
				//该座位自己有预约,进入签到签退流程
				seatScanSignUp(barCode);
			} else {
				//该座位其他人有预约或参数错误
				mui.alert(result.msg);
			}
		}
	});

}

//获取选择的座位信息
function setSelectSeatInfo(barcode) {
	mui.ajax('/mobile/ajax/seat/SeatInfoHandler.ashx', {
		data: {
			data_type: "GetSeatInfo",
			barcode: barcode
		},
		async: false,
		dataType: 'json', //服务器返回json格式数据
		type: 'post', //HTTP请求类型
		timeout: 10000, //超时时间设置为10秒；
		success: function(result) {
			//console.log(result);
			if (result.code == 0) {
				var data = JSON.parse(result.data);
				addresscode = data.Address_Code;
				seatno = data.Code;
				$('#seat_no').val(data.Code);
								
				//判断是否在阅览室开放时间范围内
				checkAddressOpenTime(data.Code,data.Name);

			} else {
				mui.alert("扫描的座位编号不存在");
			}
		},
		error: function(xhr, type, errorThrown) {
			// mui.alert(xhr.responseText);
			mui.toast("系统错误");
		}
	});
}

//判断是否在阅览室开放时间范围内
function checkAddressOpenTime(seatno,seatname){
	mui.ajax('/mobile/ajax/seat/SeatCheckHandler.ashx', {
		data: {
			data_type: "checkAddressOpenTime",
			addresscode: addresscode
		},
		async: false,
		dataType: 'json', //服务器返回json格式数据
		type: 'post', //HTTP请求类型
		timeout: 10000, //超时时间设置为10秒；
		success: function(result) {
			//console.log(result);
			if (result.code == 0) {
				//弹出座位选择框并显示状态信息
				showSeatStatus(seatno,seatname);
			} else {
				mui.toast(result.msg);
			}
		},
		error: function(xhr, type, errorThrown) {
			// mui.alert(xhr.responseText);
			mui.toast("系统错误");
		}
	});	
}
				
//弹出座位选择框并显示状态信息
function showSeatStatus(barcode,seatname) {
	mui("#popover").popover('toggle', document.getElementById("popoverDiv"));
	var jWidth = $("#popover").width();
	seatScanBookTimeScale(jWidth,seatdate); //初始化时间刻度  
	$('#selectSeatNo').html("座位编号：" + seatname);

	//获取当前座位被预约时段
	mui.ajax('/mobile/ajax/seat/SeatDateHandler.ashx', {
		data: {
			data_type: 'getSeatDate',
			seatno: barcode,
			seatdate: 'today',
		},
		type: 'post',
		async: false,
		dataType: 'json',
		timeout: 10000, //10秒超时
		success: function(result) {
			var content = "";
			//console.log(result);
			if (result.code == 0) {
				var data = JSON.parse(result.data);
				for (var i = 0; i < data.length; i++) {
					content += "【" + (data[i].ShowStart + "-" + data[i].ShowEnd) + "】 ";
				}
			} else {
				content = result.msg;
			}
			$('#havedata').html(content);
		},
		error: function(xhr, type, errorThrown) {
			mui.toast("系统错误");
		}
	});

}

//座位扫码签到签退操作
function seatScanSignUp(barCode) {
	mui.ajax('/mobile/ajax/seat/ScanHandler.ashx', {
		data: {
			data_type: "scanSign",
			barcode: barCode
		},
		async: false,
		dataType: 'json', //服务器返回json格式数据
		type: 'post', //HTTP请求类型
		timeout: 10000, //超时时间设置为10秒；
		success: function(result) {
			//console.log(result);
			if (result.code != 2) {
				mui.alert(result.msg);
			} else {
				mui.confirm("确定要提前签退吗？", "提示框", ['取消', '确定'], function(e) {
					if (e.index == 1) {
						mui.ajax('../ajax/seat/ScanHandler.ashx', {
							data: {
								data_type: "signOut",
								id: result.data
							},
							dataType: 'json', //服务器返回json格式数据
							type: 'post', //HTTP请求类型
							async: false,
							timeout: 10000, //超时时间设置为10秒；
							success: function(result) {
								mui.alert(result.msg);
							},
							error: function(xhr, type, errorThrown) {
								//  mui.toast(xhr.responseText);
								mui.toast("系统错误");
							}
						});
					}
				}, true);
			}
		},
		error: function(xhr, type, errorThrown) {
			mui.toast(xhr.responseText);
			mui.toast("系统错误");
		}
	});
};

//*黑名单及禁止预约操作判断*
function CheckBlackAndStopBook(url) {
	mui.ajax("/mobile/ajax/seat/SeatCheckHandler.ashx", {
		data: {
			data_type: 'checkBlackAndStopBook'
		},
		async: false,
		dataType: 'json', //服务器返回json格式数据
		type: 'post', //HTTP请求类型
		timeout: 10000, //超时时间设置为10秒
		success: function(result) {
			//console.log(result);
			if (result.code != 0) {
				mui.toast(result.msg);
			} else {
				mui.openWindow({
					url: url + '?v=' + new Date().getTime(),
					id: ''
				});
			}
		},
		error: function(xhr, type, errorThrown) {
			checklogin(xhr.responseText);
			mui.toast("操作失败，checkBlackList异常");
		}
	});
}

//*座位扫码预约结束时间刻度设置(一个点)*
function seatScanBookTimeScale(jWidth, seatdate) {

	mui.ajax('/mobile/ajax/seat/SeatDateHandler.ashx', {
		data: {
			data_type: 'getSeatInit',
			addresscode: addresscode,
			seatdate:seatdate
		},
		async: false,
		dataType: 'json',
		type: 'post',
		timeout: 10000, //10秒超时
		success: function(result) {
			console.log(result);
			if (result.code == 0) {
				var data = JSON.parse(result.data);
				var starttime = parseInt(data[0].sTime);
				var endtime = parseInt(data[0].eTime);
			 	var step = parseInt(data[0].BookTimeScale); 
				var scaledatastr = data[0].ScaleData; 
				var scaledata = scaledatastr.split(",");
				
				$('#inittime').jRange({
					from: starttime,   //最小值
					to: endtime,  //最大值
					step: step,
					scale: scaledata,  //刻度条
					format: '%s',   //设置标签格式
					width: jWidth * 0.85,  //宽度
					showLabels: true,  //显示在滑块顶部的标签
					showScale: false, //显示滑块下方显示的比例标签
					snap: true   ,//是否只允许按增值选择(默认false)					
				}); 
				
			} else {
				mui.toast(result.msg);
			}

		},
		error: function(xhr, type, errorThrown) {
			//异常处理；
			//console.log(type);
			//console.log(xhr.responseText);
			//checklogin(xhr.responseText);
			mui.toast("数据初始化失败");
		}
	});
}

//*座位预约时间刻度设置(两个点)*
function setBookTimeScale(jWidth,seatdate) {
	mui.ajax('/mobile/ajax/seat/SeatDateHandler.ashx', {
		data: {
			data_type: 'getSeatInit',
			addresscode: addresscode,
			seatdate:seatdate
		},
		async: false,
		dataType: 'json',
		type: 'post',
		timeout: 10000, //10秒超时
		success: function(result) {
			//console.log(result);
			if (result.code == 0) {
				var data = JSON.parse(result.data);
				var starttime =  parseInt(data[0].sTime);
				var endtime = parseInt(data[0].eTime);
			 	var step = parseInt(data[0].BookTimeScale);
				var scaledatastr = data[0].ScaleData; 
				var scaledata = scaledatastr.split(",");
				$('#inittime').val("" + starttime + "," + endtime + "");
				$('#inittime').jRange({
					from: starttime,   //最小值
					to: endtime,  //最大值
					step: step,
					scale: scaledata,  //刻度条
					format: '%s',   //设置标签格式
					width: jWidth * 0.85,  //宽度
					showLabels: true,  //显示在滑块顶部的标签
					showScale: false, //显示滑块下方显示的比例标签
					isRange: true,  //是否为范围(默认false,选择一个点),如果是true，选择的是范围,格式为'1,2'
					snap: true   //是否只允许按增值选择(默认false)
				});  
			} else {
				mui.toast(result.msg);
			}
		},
		error: function(xhr, type, errorThrown) {
			//异常处理；
			//console.log(type);
			//console.log(xhr.responseText);
			//checklogin(xhr.responseText);
			mui.toast("数据初始化失败");
		}
	});
}

//*检测是否有地图*
function checkMap(address_code) {
	var map = "";
	//判断是否具备预约权限
	mui.ajax('../../ajax/seat/SeatCheckHandler.ashx', {
		data: {
			data_type: "checkMap",
			address_code: address_code
		},
		async: false,
		dataType: 'json', //服务器返回json格式数据
		type: 'post',
		timeout: 10000, //10秒超时
		success: function(data) {
			map = data;
		},
		error: function(xhr, type, errorThrown) {
			// console.log(type);
			//console.log(xhr.responseText);
			checklogin(xhr.responseText);
			mui.toast('获取数据失败');
			//TODO 此处可以向服务端告警
		}
	});

	return map;
}
