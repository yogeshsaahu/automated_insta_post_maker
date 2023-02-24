from PIL import Image,ImageFilter,ImageDraw,ImageFont
import textwrap
import uuid

class PostMaker:

        def maker(self, data):
            temp = []
            for i in data:
                title = i["heading"]
                image = i["img"]
                if image == None:
                    temp.append(image)

                else:
                    print(i["count"])
                    # image = Image.open(image)
                    self.create_post(image, title)
                    print("post created")

        def crop_image(self, image):
            print(image)
            image = Image.open(r"{}".format(image))
            width, height = image.size
            if width == height:
                return image
            offset = int(abs(height-width)/2)
            if width>height:
                image = image.crop([offset,0,width-offset,height])
            else:
                image = image.crop([0,offset,width,height-offset])

            image = image.filter(ImageFilter.GaussianBlur(2))

            return image



        def create_post(self,image,title):

                image = self.crop_image(image)
                astr = title
                para = textwrap.wrap(astr, width=30)
                MAX_W, MAX_H = 388, 388

                im = image
                draw = ImageDraw.Draw(im)
                font = ImageFont.truetype('arial.ttf', 20,)

                stroke_color = ("#ffffff")

                current_h, pad = 160, 10
                for line in para:
                    w, h = draw.textsize(line, font=font)
                    draw.text(((MAX_W - w) / 2, current_h), line, font=font, stroke_width=1, stroke_fill=stroke_color, fill=(0, 0, 0))

                    current_h += h + pad

                title = uuid.uuid4().hex
                im.save(f'result/{title}.jpg')

