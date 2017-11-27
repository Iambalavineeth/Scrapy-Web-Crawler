'''
This is a Web Crawler for Incontinence's NAFC Website - A Care giving website where users post about Incontinence
NAFC Caregiver's Website ---- http://forum.nafc.org/
'''

import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.spiders import BaseSpider
from scrapy.http import FormRequest
from loginform import fill_login_form
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class UserSpider(scrapy.Spider):
    name = 'userspider'
    start_urls = ['http://forum.nafc.org/login/']
    #Getting the list of usernames
    user_names = ['livhay05', 'Benfrank', 'jason181', 'dedevz', 'PEP', 'Ashleyallday', 'Dependsareok', 'angelpisces1983', 'msuspartan', 'oakbark', 'klosk', 'NAFC', 'Patrick', 'amy', 'Janlol', 'Cheryl', 'anita', 'leaky', 'inconninmiss', 'NoCans', 'joepizzulo', 'nwyenko', 'Damp', 'Boopa0586', 'Danman', 'AtlantaGuy41', 'JWT', 'andy1050', 'Daco4', 'Joey2000', 'MikeJames', 'Tharun', 'Nazsnaz', 'nvbob', 'KBKid', 'pharmec', 'bqmedical', 'Bonnie', 'formom', 'klcox', 'Skinnyb', 'dallasguy', 'KEMYST', 'Jay', 'Sharon812', 'Susiecue', 'destinylyng', 'Laura', 'Boomersway', 'notarobot', 'Johnwatrin', 'cmulwee', 'Pbk123', 'dougsbc', 'CPFuller', 'Tarek', 'Dallasinc', 'Ozarkmtn', 'jeffswet', 'mhsahaydri', 'Derek53', 'ASQ', 'stonne168', 'pek1134', 'lucyandhercat', 'robt', 'Wearingnow', 'Jaytee', 'melupus', 'DPCARE', 'Petejc', 'NETCH', 'Ladidee', 'Spaz', 'chaps54', '6932bansheeatv', 'ron1990', 'sharian7', 'dedutch', 'dkingsb', 'jujubee22', 'ajh3677', 'PeapodMats', 'drewray', 'needanswers', 'Sylvia', 'gbannister', 'LovelyPhoenix', 'Kyan27', 'sunflower239', 'PBJ32', 'matttyco', 'wkwbwz6w', 'greengold4', 'archerstaley', 'Mightychi', 'Lee', 'Bldarden', 'melanie', 'sport', 'Billy7', 'RapperG', 'Carladams', 'glenn77', 'myrebel1980', 'Darceyyyy', 'kenedmunds', 'louellajoan', 'Mikewest440', 'Sonya', 'Jimmyjames', 'Deljordan', 'Atlantasailor', 'Connor', 'bosoxpats', 'fieldworklaoc', 'Reese', 'Seanocostigan', 'Vestalm', 'TWashington', 'Highandinside', 'Doubleic', 'Darrell', 'dan723', 'hello123', 'Kane1', 'Worrieswhynow', 'Alexandraariche', 'wilmaganda66', 'Brian30', 'knowdog', 'victorie', 'Mtnlakes', 'kattyknhugh', 'Bobby103', 'missyk', 'Debra', 'Diana', 'beatrice1', 'APRILPARIS', 'MaineSkier', 'kruciphix', 'CMcK', 'Lisafrank', 'Britt182', 'skyblue0331', 'needhelp', 'kfg4279', 'Banksallen', 'Badger', 'patrusky', 'Ethan', 'ProtexMedical', 'Youngactiveman', 'Jgsvch', 'PictureSound', 'shawshank', 'Ridge', 'James', 'bedwetter63701', '63gege63', 'gelu65', '50yobedwetr', 'Pbrown7', 'jack329', 'dorothysue', 'Sardine', 'Valeria', 'Graham', 'Annie', 'starshinespike', 'jaredc3', 'RRRN', 'Playaman', 'Boulder77', 'Mike', 'vft', 'Vasilikipapa', 'Japan_Grandma', 'BarrySimpson94', 'AnastasiaV', 'praylow', 'CARE', 'SoCalDude', 'linlou068', 'LadyBugz1', 'imanigirl', 'Weimrescuelady', 'manhattanmom', 'Indy1993', 'frenchco', 'ummulkhayr23', 'culueg77', 'ZoeMax', 'flexwing', 'AZincon', 'cpfielding', 'baton999', 'jean313', 'Allendrench', 'ShawnP', 'urinationproblem33', 'lovegirl1212', 'joel_m', 'bns39', 'Heather', 'Brian22', 'ann', 'Susan', 'Droe', 'emmittsmommom', 'soggy', 'Qwerty1', 'Ash12', 'dad3601', 'Flip', 'robinducci', 'darlene', 'dannie61', 'Rebel', 'mia', 'quinnr60', 'Mo2806', 'Debbie', 'Shawnette', 'Msman', 'itsmaddy95', 'RuralRoamer', 'rob1552', 'jeany', 'Keiko', 'Maggie', 'Suelarson', 'rondom', 'Jdelarosa', 'oakie', 'allens', 'mrsrudden1978', 'newmom14', 'kriscis', 'yomike951', 'daysgone', 'Preston', 'MusicLover678', 'Nicole', 'torontostarboy', 'OABResearch', 'Blingyxo', 'Pennysmith89', 'rastil', 'Offcons', 'Bobaan48', 'reny30', 'Hotdogg55', 'CardioAnna', 'johnroba1', 'sputnik', 'wondering', 'hubbub']

    def __init__(self, *args, **kwargs):
        super(UserSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return [FormRequest.from_response(response,
                    formdata={'registerUserName': 'helloworld123', 'registerPass': 'helloworld123'},
                    callback=self.after_main_login)]

    def after_main_login(self, response):
        for user in self.user_names:
            user_url = 'profile/' + user
            yield response.follow(user_url, callback=self.parse_user_pages)

    def parse_user_pages(self, response):
        yield{
            "USERNAME": response.xpath('//div[contains(@class, "main") and contains(@class, "no-sky-main")]/h1[contains(@class, "thread-title")]/text()').extract_first(),
            "UPVOTES": response.xpath('//div[contains(@class, "proUserInfoLabelLeft") and @id="proVotesCap"]/text()').extract_first(),
            "JOIN-DATE": response.xpath('//div[contains(@class, "proJoined")]//text()').extract()[1],
            "LOCATION": response.xpath('//div[contains(@class, "proExtLinks")]/div[contains(@class, "proExtLink") and div/text()="Location"]/div[contains(@class, "proExtLinkValue")]/a/text()').extract_first(),
            "HOMEPAGE": response.xpath('//div[contains(@class, "proExtLinks")]/div[contains(@class, "proExtLink") and div/text()="Homepage"]/div[contains(@class, "proExtLinkValue")]/a/text()').extract_first(),
            "FACEBOOK": response.xpath('//div[contains(@class, "proExtLinks")]/div[contains(@class, "proExtLink") and div/text()="Facebook"]/div[contains(@class, "proExtLinkValue")]/a/text()').extract_first(),
            "TWITTER": response.xpath('//div[contains(@class, "proExtLinks")]/div[contains(@class, "proExtLink") and div/text()="Twitter"]/div[contains(@class, "proExtLinkValue")]/a/text()').extract_first(),
            "LINKEDIN": response.xpath('//div[contains(@class, "proExtLinks")]/div[contains(@class, "proExtLink") and div/text()="LinkedIn"]/div[contains(@class, "proExtLinkValue")]/a/text()').extract_first(),
            "INSTAGRAM": response.xpath('//div[contains(@class, "proExtLinks")]/div[contains(@class, "proExtLink") and div/text()="Instagram"]/div[contains(@class, "proExtLinkValue")]/a/text()').extract_first()
        }

if __name__ == "__main__":
    spider = UserSpider()
# import scrapy
#
#
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 "TEXT": response.xpath('//div[contains(@class, "quote")]/span[contains(@class, "text")]/text()').extract_first(),
#                 "AUTHOR": quote.css('small.author::text').extract_first(),
#                 "tags": quote.css('div.tags a.tag::text').extract(),
#             }
