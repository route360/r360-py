from src.util.TravelOptions import TravelOptions

travelOptions = TravelOptions();
travelOptions.setServiceUrl('https://service.route360.net/germany/')

print(travelOptions.getServiceUrl())