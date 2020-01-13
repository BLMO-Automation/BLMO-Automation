
class Locator(object):
    # Logindex page
    usename = '//input[@name="username"]'
    password = '//input[@name="Password"]'
    roleCombo = '//*[@id="isc_1F"]'
    roleAdmin = '//*[@id="isc_PickListMenu_0_row_0"]'
    sigin = '//*[@id="isc_1L"]'


    # Home Page tool strip
    toolStrip = '//*[@class="toolStrip"]'
    logOut = '//img[contains(@src,"images/logout.png")]'

    # Home Page side Stack
    sStack = '//*[@class="sectionStack"]'
    bandwidth = '//*[@class="imgSectionHeaderTitleclosed"]//*[text()="Bandwidth Management"]'
    security = '//*[@class="imgSectionHeaderTitleclosed"]//*[text()="Security"]'
    systemConfiguration = '//*[@class="imgSectionHeaderTitleclosed"]//*[text()="System Configuration"]'
    notifications = '//*[@class="imgSectionHeaderTitleclosed"]//*[text()=Notifications"]'
