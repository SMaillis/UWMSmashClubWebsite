
            const span = document.getElementById('time_left');
            const element = document.getElementById('days');
            var day = parseInt(element.dataset.daysLeft);
            console.log("Days left:", day);
            var curTime = new Date();
            const isDST = new Date("June 1, 2025 00:00:00");
            const notDST = new Date("January 1, 2025 00:00:00");

            //get the timezone offset for the user so the time displays correctly regardless of if its DST or not
            function calcOffset(time){
                //get the month, march is 2, november is 10
                var month = time.getMonth();
                var dayOfMonth = time.getDate();
                var year = time.getFullYear();

                //if month is between march and november to see if we are in daylight savings
                if(month >= 2 && month <= 10){

                    if(month === 2) {
                        var marchDate = new Date("March 1, " + year + " 00:00:00");
                        var daysToSunday;

                        //get the 2nd sunday of march
                        if (marchDate.getDay() !== 0) {
                            daysToSunday = (7 - marchDate.getDay());
                        }
                        daysToSunday += 7;
                        var dlsStartDate = 1 + daysToSunday;

                        //now see if our current date is after the start of daylight savings
                        if(dlsStartDate <= dayOfMonth){
                            return 300;
                        }
                        else {
                            return 360;
                        }

                    }
                    else if(month === 10) {
                        var novemberDate = new Date("November 1, " + year + " 00:00:00");
                        //get the 1st sunday of november
                        var tempDate = novemberDate.getDay();
                        daysToSunday = 0;
                        if (tempDate !== 0) {
                            daysToSunday += (7 - tempDate)
                        }
                        var dlsEndDate = 1 + daysToSunday;

                        if(dlsEndDate > dayOfMonth){
                            return 300;
                        }
                        else {
                            return 360;
                        }
                    }
                    else {
                        return 300;
                    }
                }
                return 360;
            }

            //this is used to get the bracket hour
            var DST = calcOffset(curTime);
            let offset = (DST - curTime.getTimezoneOffset()) / 60;

            //this value checks if the user is in a non-daylight savings time country, if they are then set to 1
            var nonDSTCountry = 0;
            if (isDST.getTimezoneOffset() === notDST.getTimezoneOffset())
            {
                nonDSTCountry = 1;
            }

            function getTimeLeft(){
                //testing stuff
                curTime = new Date(curTime.valueOf() + 1000);
                console.log(curTime);

                //get the hours digit
                var bracketHour = 16 + offset;

                //check if the user's country uses daylight savings time, if they don't then subtract
                //1 if daylight savings time isn't going on


                if(bracketHour >= 24){ bracketHour -= 24; }

                var hour;
                if(curTime.getHours() <= bracketHour){
                    hour = bracketHour - curTime.getHours();
                }
                else {
                    hour = bracketHour + 24 - curTime.getHours();
                }
                if(DST === 360) {
                    hour -= nonDSTCountry;
                }


                //check to see if minutes is at 30, if it is then subtract 1 from hour
                if(curTime.getMinutes() > 29) {
                    hour -= 1

                    //if it is 4 pm and after 30 minutes prevent the value from displaying as a negative
                    if(hour === -1) { hour += 24 }
                }

                //get the minutes digit
                var minute;
                if(curTime.getMinutes() <= 29) {
                    minute = 29 - curTime.getMinutes();
                } else {
                    minute = 89 - curTime.getMinutes();
                }

                //get the seconds digit
                var second;
                if (curTime.getSeconds() === 0) {
                    second = curTime.getSeconds();
                } else {
                    second = 60 - curTime.getSeconds();
                }

                //fixing roll over issues
                //make sure the minute doesn't roll over until seconds is past 00
                if(second === 0)
                {
                    //make sure the clock doesn't display 60 minutes
                    minute += 1;
                    if(minute === 60) { minute = 0 }

                    //make sure that the hour doesn't roll over when minutes and seconds are 00
                    if(minute === 0){
                        hour += 1;
                        if (hour === 24) { hour = 0 }
                    }
                }

                //if the hour, minute, and seconds all roll over, then subtract 1 from day
                if(hour === 23 && minute === 59 && second === 59){
                    day -= 1;
                    if(day === -1) { day = 6 }
                }

                //set the clock to display properly, if the current time is during the bracket then display that
                //the bracket is underway instead of the time left
                if(day === 6 && hour >= 18 && (minute >= 30 || hour > 18))
                {
                    span.textContent = "The Bracket is Currently Underway";
                }
                else {
                    span.textContent = ("0" + day).slice(-2) + ":" + ("0" + hour).slice(-2) + ":" +
                        ("0" + minute).slice(-2) + ":" + ("0" + second).slice(-2) + "   " + offset;
                }
            }

            //call the function at the end to ensure that it actually runs, we use a set interval so it updates every second
            setInterval(getTimeLeft, 1000);