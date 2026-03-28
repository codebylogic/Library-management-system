# मैंने सबसे पहले लाइब्रेरी क्लास बनाया लाइब्रेरी क्लास इसलिए बनाया क्योंकिअगर दो-तीन लाइब्रेरी बनाना हो तोवाइल लूप इफैक्ट्ससे कोड बहुत उलझ जाएगाकोड को क्लीन रखने के लिए मैंनेउप्स का इस्तेमाल किया है
class Labrabry:
    def __init__(self):
        self.book=[]
        self.no_of_book=0
        
        # बुक ऐड करने वाला डेफिनेशन बनाया
    def add_book(self):
        new_book=input("enter book name: ") #यूजर्स इनपुट लेने के लिए की बुक का नाम क्या है
        self.book.append(new_book)
        self.no_of_book +=1 #बुक की संख्या बढ़ाने के लिए
        #बुक रीड करने वाला डेफिनेशन बनाया
    def view_labrbry(self):
      #फॉर लूप बुक को एक-एक करके अच्छे से सजा के प्रिंट करेगा
        print("----labrabry ka sabhi book-----")
        for b in self.book:
            
            print(f"{b}")
        print("="*15)  
        print(f"total book is {self.no_of_book}")
my_labrbry=Labrabry()
while True:#इसको हम while True के अंदर इसलिएकर रहे हैं ताकि यूजर जब तक यूजर no ना दबा देतब तक प्रोग्राम चलते रहे
    
    my_labrbry.add_book()#बुक ऐड करने वाला डेफिनेशन को कॉल किया
    my_labrbry.view_labrbry()#बुक दिखाने वाला डेफिनेशन को कॉल किया
    ask=input("kya aap or book add kerna chahte hai(answer in yes or no)").lower() #यूजर से पूछने के लिए की क्या हुआ और बुक ऐड करना चाहता है और उसे लवर कर दिया ताकि प्रोग्राम उसकोस्मॉल लेटर में कन्वर्ट कर दे
    
    if ask=='no':# यूजर से पूछा जाए कि वह और किताब ऐड करना चाहते हैं या नहींअगर यूजर no दबा दें तो प्रोग्राम बंद हो जाए
        break