# Create your views here.
import os
from PIL import Image, ImageFont, ImageDraw
import phonenumbers
from core.aastra.ImageScreen import AastraIPPhoneImageScreen
from core.views import AastraView, AastraResponseMixin
from visiblenumbers.settings import SERVER_IMAGE_PHONE_URL


class ShowNumbers(AastraResponseMixin, AastraView):


    def get(self, request, *args, **kwargs):
        phone_number_text = request.GET.get('number')
        if phone_number_text.startswith('00') or phone_number_text.startswith('+'):
            number_dict = phonenumbers.parse(request.GET.get('number'), None)
        if phone_number_text.startswith('0'):
            phone_number_text = phone_number_text[1:]
        #check the incoming number
        file_path = os.path.join(os.path.dirname(__file__), '..', 'static/%s.png'%phone_number_text).replace('\\','/')
        if not os.path.exists(file_path):
            img=Image.new("RGB", (640,480),(255,255,255))
            fontFile = os.path.join(os.path.dirname(__file__), '..', 'fonts/tiresias.ttf').replace('\\','/')
            font_size = 1
            img_fraction = 0.97
            font = ImageFont.truetype(fontFile,font_size)

            while font.getsize(phone_number_text)[0] < img_fraction*img.size[0]:
                font_size += 1
                font = ImageFont.truetype(fontFile,font_size)

            draw = ImageDraw.Draw(img)
            draw.text((8, 130),phone_number_text,(0,0,0),font=font)
            img.save(os.path.join(os.path.dirname(__file__), '..', 'static/%s.png'%phone_number_text).replace('\\','/'))

        aastra_image = AastraIPPhoneImageScreen(timeout="10",mode="fullscreen",destroyOnExit="yes")
        aastra_image.add_image("480","640","%s/%s"%(SERVER_IMAGE_PHONE_URL,'%s.png'%phone_number_text), verticalAlign="top", horizontalAlign="left")
        xml_code = aastra_image.getXML()
        return self.render_to_response(xml_code)