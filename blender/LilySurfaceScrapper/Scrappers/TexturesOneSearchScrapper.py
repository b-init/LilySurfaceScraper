# Copyright (c) 2019 Bent Hillerkus

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from .TexturesOneScrapper import TexturesOneScrapper
from .AbstractScrapper import AbstractScrapper
from random import choice

class TexturesOneSearchMaterialScrapper(TexturesOneScrapper):
    scrapped_type = "MATERIAL"
    scrapped_type_name = "tex-pbr"
    supported_creators = [1, 2, 4] # IDs of the websites on Textures.one that we support

    @classmethod
    def searchForTexture(cls, search_term):
        url = "https://textures.one/search/?q=" + search_term + "&" + cls.scrapped_type_name
        html = AbstractScrapper.fetchHtml(None, url)
        options = html.xpath("//div[@class='indexBox']")
        options = list(filter(lambda o : any("/" + str(p) + "/" in str(o.xpath(".//div/div")[1].xpath(".//img/@src")) for p in cls.supported_creators) , options))
        links = list(map(lambda o:str(o.xpath(".//a/@href")[0]), options))
        return choice(links)

    @classmethod
    def canHandleUrl(cls, search_term):
        return super().canHandleUrl(cls.searchForTexture(search_term))

class TexturesOneSearchWorldScrapper(TexturesOneSearchMaterialScrapper):
    scrapped_type = "WORLD"
    scrapped_type_name = "hdri-sphere"
    supported_creators = [3]
