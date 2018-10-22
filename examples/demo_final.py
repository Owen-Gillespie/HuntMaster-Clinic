import seek
DOMAIN = "seek-165508.appspot.com"
info_lat = 33.781310999999995
info_long = -118.1131253
bicycle_image = '/static/img/bicycle_image.JPG'

start = seek.StartModule(('<p> Somebody on the HuntMaster team has pushed the results of this abomination </p>'
                            '<img src="/static/img/start_picture.png" alt="git commit -m "Kind of lost, heading to the information booth...">'),
                            'Find-the-info-center')
find_info = seek.GPSModule('Find-the-info-center','At-the-info-center',info_lat,info_long)
QR = seek.QRModule('At-the-info-center', ('<p> As you arrive at the information center, you see a suspicious figure leaving the scene. Before you attempt to apprehend the figure,'
                           ' you notice a QR code...</p>'),'What-the-QR-code-says',DOMAIN)
QR_info = seek.ContentModule('What-the-QR-code-says','<p> Reading the resulting webpage you obtained from the QR code, you find that there is hidden information' +
                            ' embedded in an image nearby.</p>' + '<img src="' + bicycle_image + '" alt="bicycle" height="665" width="500">','Take-a-picture')
take_picture = seek.ImageMatchModule('Take-a-picture', 'What-the-picture-says', bicycle_image)
picture_info = seek.ContentModule('What-the-picture-says','<p> Hidden in the image is the revelation that the perpetrator is fond of soda. Lay out a can'
                            ' as bait and catch him! </p>','Lay-out-the-bait')
set_bait = seek.FindObjectModule('Lay-out-the-bait', 'Whodunnit', 'drink')
whodunnit = seek.TextInputModule('Whodunnit','end','Cole')

print start
print find_info
print QR
print QR_info
print take_picture
print picture_info
print set_bait
print whodunnit
seek.save_module_data()
