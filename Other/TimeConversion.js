function timeCon(time){
	if(time.substring(8, 10) === "PM"){
		if(time.substring(0, 2) === "12"){
			console.log(time.substring(0, 8));
		} else{
			var hour = parseInt(time.substring(0, 2)) + 12;
			console.log(hour.toString() + time.substring(2, 8));
		}
	} else{
		if(time.substring(0, 2) === "12"){
			console.log("00" + time.substring(2, 8));
		} else{
			console.log(time.substring(0, 8));
		}
	}
}

timeCon("12:10:50AM");
timeCon("01:02:49AM");
timeCon("11:00:10AM");
timeCon("12:00:00PM");
timeCon("06:38:19PM");