import seek
DOMAIN = "http://127.0.0.1:5000"
info_lat = 33.78130180915361
info_long = -118.11316083436564
bicycle_image = '/static/img/bicycle_image.JPG'

start = seek.StartModule(('<p> Somebody on the HuntMaster team has pushed the results of this abomination </p>'
                            '<img src="/static/img/start_picture.png" alt="git commit -m "Kind of lost, heading to the information booth...">'),
                            'Find-the-info-center')
find_info = seek.GPSModule('Find-the-info-center','At-the-info-center',info_lat,info_long, 60000)
QR = seek.QRModule('At-the-info-center', ('<p> As you arrive at the information center, you see a suspicious figure leaving the scene. Before you attempt to apprehend the figure,'
                           ' you notice a QR code...</p>'),'What-the-QR-code-says','content', DOMAIN)
picture_info = seek.ContentModule('What-the-QR-code-says','Embedded in the QR code is the revelation that the perpetrator is fond of soda. Lay out a can'
                            ' as bait and catch him! </p>','Lay-out-the-bait')
whodunnit = seek.TextInputModule('Lay-out-the-bait','end','Cole')

seek.save_module_data()
