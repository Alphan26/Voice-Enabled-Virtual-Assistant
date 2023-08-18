import xml.etree.ElementTree as ET
from speech_2_text import answer

# We will import the variable called answer from speech_2_text.py file such that we will give answer due to the users
# response.

# Create the root
root = ET.Element("Response")

child1 = ET.SubElement(root, "Child1")
child1.text = "Merhaba, jeton wallet tan arıyorum. Aracınız hakkında sigorta fırsatlarımız konusunda bilgi vermemi " \
              "ister" \
              " misiniz ?"

# Listening operation starts now.
# Now, we need to listen the response of the customer.

if answer == 1:  # This means that customer wants to get information about the car insurance
    child2 = ET.SubElement(root, "Child2")
    child2.text = "Tabiki, bunun için sırasıyla isim soyisminize, TC kimlik numaranıza ve araba plakanıza " \
                  "ihtiyacım var. Bu şekilde size en uygun fırsatları sunabilirim."

else:  # That means the customer doesn't want to be bothered and wants to hang up the phone.
    child3 = ET.SubElement(root, "Child3")
    child3.text = "Anladım, vakit ayırdığınız için teşekkür ederim, iyi günler dilerim."

# Now the system needs to get the identity number and car plate number respectively. Afterward, it will give the
# response accordingly.

child4 = ET.SubElement(root, "Child4")
# The content of the child4 will be dynamic since each car has different type of car insurance.

child4.text = " Verdiğiniz bilgilere göre, A sigortadan " \
              "500 TL ye sigorta yaptırabilirsiniz. B sigortada ise 350 TL'ye sigorta yaptırabilirsiniz.\n\nBu " \
              "bilgileri " \
              "size sms olarak gönderiyorum. daha detaylı görüşme için lütfen şirketle iletişime geçiniz, " \
              "iyi günler dilerim."

# make the XML file
tree = ET.ElementTree(root)
tree.write("speech_flow.xml", encoding="utf-8", xml_declaration=True)
