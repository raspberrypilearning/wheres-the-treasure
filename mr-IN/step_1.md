## परिचय

या प्रोजेक्ट मध्ये मेमरी गेम खेळण्यासाठी आपण Sense HAT वर जॉयस्टिक आणि एलईडी मॅट्रिक्सचा वापर कराल. Sense HAT सोन्याचे नाणे दर्शवेल आणि आपल्याला ते कोठे आहे हे आठवण ठेवायचे आणि लपवलेला खजिना शोधण्यासाठी जॉयस्टिक वापरणे आवश्यक आहे.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/79ac6a377d?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark">
</iframe> <img src="images/treasure-final.png" />
</div>

गेम खेळण्यासाठी run दाबा आणि पिवळा ठिपका कोठे दिसतो ते पहा - हा खजिना आहे! नंतर खजिना कोठे असावा ते शोधण्या साठी कीबोर्ड वरील एरो की द्वारे पांढरा बिंदू हलवा. तिथे पोहोचल्यावर रीटर्न दाबा. आपण योग्य असल्यास आपल्याला हिरवा ठिपका आणि एखादी चूक झाल्यास लाल ठिपका दिसेल. आपल्याला 10 प्रयत्न आणि नंतर 10 पैकी एक स्कोअर मिळेल.

लक्षात घ्या की Sense HAT एमुलेटर वापरताना आपण Sense HATवर जॉयस्टिकच्या ऐवजी एरो आणि रीटर्नचा वापर कराल.

### क्लब प्रमुखांसाठी अधिक माहिती

तुम्हाला हा प्रकल्प प्रिंट करण्याची आवश्यकता असल्यास, कृपया [प्रिंट अनुकूल आवृत्ती](https://projects.raspberrypi.org/mr-IN/projects/wheres-the-treasure/print) वापरा.

--- collapse ---
---
title: क्लब प्रमुखांसाठी टिपा
---

## परिचय:

या प्रोजेक्ट मध्ये, मुले मेमरी गेम तयार करण्यासाठी Sense Hat जॉयस्टिकचा कसा वापर करावा हे शिकतील. Sense HAT सोन्याचे नाणे दर्शवेल आणि आपल्याला ते कोठे आहे हे आठवण ठेवायचे आणि लपवलेला खजिना शोधण्यासाठी जॉयस्टिक वापरणे आवश्यक आहे.

## ऑनलाईन संसाधने

**या प्रोजेक्ट मध्ये Python 3 चा उपयोग केला जातो**. आम्ही Python ऑनलाइन लिहिण्या साठी [Trinket](https://trinket.io/) चा वापर करण्याची शिफारस करतो. या प्रोजेक्ट मध्ये पुढील Trinkets आहेत:

* ['खजिना कुठे आहे?' स्टार्टर trinket - jumpto.cc/treasure-go](http://jumpto.cc/treasure-go)

पूर्ण झालेले प्रोजेक्ट असलेले एक trinket देखील आहे:

* [' खजिना कोठे आहे' समाप्त - trinket.io/python/79ac6a377d](https://trinket.io/python/79ac6a377d)

## ऑफलाइन संसाधने

हा प्रोजेक्ट Raspberry Pi संगणका बरोबर एका Sense Hat सह [ऑफलाइन](https://www.codeclubprojects.org/en-GB/resources/physical-sense-hat/) देखील पूर्ण केला जाऊ शकतो. तुम्ही या प्रोजेक्टचे संसाधने 'Project Materials' च्या लिंक वर​ क्लिक करून मिळवू शकता. या लिंक मध्ये 'Project Resources' विभाग आहे, ज्यामध्ये मुलांना हा प्रोजेक्ट ऑफलाइन पूर्ण करण्यासाठी आवश्यक असणारी संसाधने आहेत. प्रत्येक मुलाकडे ह्या संसाधनांची एक प्रत असेल ह्याची खात्री करा. या विभागात खालील फायली समाविष्ट आहेत:

* treasure/treasure.py

ह्या प्रोजेक्टची पूर्ण झालेली आवृत्ती तुम्हाला 'Volunteer Resources' विभागात मिळेल ज्यात हे आहे:

* treasure-finished/treasure.py

(वरील सर्व संसाधने प्रोजेक्ट आणि वोलंटीर `.zip` फायली म्हणून डाउनलोड करण्यायोग्य देखील आहेत.)

## शिकण्याचे उद्दिष्टे

* Sense HAT जॉयस्टिक;
* Boolean logic;

या प्रोजेक्ट मध्ये [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum) चे खालील घटक समाविष्ट आहेत:

* [समस्या सोडवण्यासाठी प्रोग्रामिंग संकल्पना एकत्र करा.](https://www.raspberrypi.org/curriculum/programming/builder)

## Challenges

* गेम सानुकूलित करा - भिन्न रंग वापरा किंवा टेक्स्ट संदेश जोडा. 
* अधिक कठिण बनवा - लपवलेले नाणे दाखवल्यानंतर नाणी कमी वेळा करिता दर्शवा किंवा नाणे दाखवून खेळाडूंना गोंधळ घाला. 

--- /collapse ---

--- collapse ---
---
title: प्रोजेक्ट साहित्य
---

## प्रोजेक्ट संसाधने

* [सर्व प्रोजेक्टची संसाधने असलेली.zip फाइल](resources/treasure-project-resources.zip)
* [स्टार्टर प्रोजेक्ट](http://jumpto.cc/treasure-go)
* [ऑफलाइन स्टार्टर Python फाइल](resources/treasure-treasure.py)

## क्लब लीडर साठी संसाधने

* [सर्व पूर्ण झालेली प्रोजेक्ट संसाधने असलेली.zip फाइल](resources/treasure-volunteer-resources.zip)
* [ऑनलाइन पूर्ण झालेले Trinket प्रोजेक्ट](https://trinket.io/python/79ac6a377d)
* [treasure-finished/treasure.py](resources/treasure-finished-treasure.py)

--- /collapse ---