def add_time(start, duration, day = None):
  
  # First I get the hours, minutes and AM/PM and store them.
  
  startHour = int(start.split(":")[0])
  startMinutes = int(start.split(":")[1].split()[0])
  z = start.split(":")[1].split()[1]

  # Same for the duration
  hoursPassed = int(duration.split(":")[0])
  minPassed = int(duration.split(":")[1])

  # I calculate the final minutes and check if an hour has passed by.
  finalMin = startMinutes + minPassed
  if finalMin >= 60:
    startHour += 1
    finalMin = finalMin - 60

  # Here I calculate the final hour, checking whether is Am or PM starting time and also keeping track of the days that passed
    
  if z == 'PM':
    startHour += 12
  
  finalHour = startHour + hoursPassed
  
  daysPassed = 0
  
  if finalHour >= 24:
    daysPassed = int(finalHour / 24)
    finalHour = finalHour % 24
  
  zz = 'AM'
  if finalHour == 0:
    finalHour = 12
  elif finalHour == 12:
    zz = 'PM'
  elif finalHour > 12:
    finalHour -= 12
    zz = 'PM'

  # Here I build the string depending on the number of days that passed
  if daysPassed == 0:
    text = ""
  elif daysPassed == 1:
    text = " (next day)"
  else:
    text = f" ({daysPassed} days later)"

  # Here is the logic in case we have an starting day given to us
  days = {1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday', 7 : 'Sunday'}

  
  if day != None:
    dayNum = list(days.keys())[list(days.values()).index(day.capitalize())]
    
    if dayNum + daysPassed > 7:
      dayNum += daysPassed % 7
    else:
      dayNum += daysPassed
    
    finalDay = days[dayNum]

  # Finally I return the string with or without the name of the day
  if day != None:
    new_time = f"{finalHour}:{finalMin:02d} {zz}, {finalDay}" + text
  else:
    new_time = f"{finalHour}:{finalMin:02d} {zz}" + text



  


  return new_time