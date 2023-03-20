t= eval(input('輸入今天溫度：'))
aqi= eval(input('輸入今天AQI:'))

if t>=37 or aqi>=150:
    print("避免外出")
else:
    print("可依需要待在戶外")
    
