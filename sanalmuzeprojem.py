# Melike Çağlar 234210022 

import numpy as np # gerekli kütüphaneler
import getpass
import webbrowser

gorevliler = [] #Global listeleri tanımladım
kullanıcıDegerlendirmeleri = np.array([])
kullanıcıBilgileri = []
yoneticiGBilgileri = ("melike","1234")
yorumVeritabani = []
minyatürler = { # minyatürler listesi
    1: {"yazar": "matrakçı nasuh", "tarihi": 1501, "aciklama": "Ayasofya minyatürü, Osmanlı minyatür sanatının ve İstanbul'un tarihi dokusunun önemli bir örneğidir. Sanatçı, bu minyatürde Ayasofya'nın mimari güzelliklerini ve tarihi önemini başarılı bir şekilde yansıtmıştır"},
    2: {"yazar": "anonim", "tarihi": 1301, "aciklama": "Notre Dame Katedrali'nin minyatürleri, genellikle Orta Çağ ve Rönesans dönemlerinde yapılmıştır. Minyatürler, Notre Dame Katedrali'nin mimari güzelliklerini ve tarihsel önemini vurgulayan değerli sanatsal eserlerdir."},
    3: {"yazar": "anonim", "tarihi": None, "aciklama": "Edinburgh Kalesi'nin minyatürü, kalenin mimarisini ve tarihini detaylı bir şekilde açıklamak, eğitim vermek, turistik bilgi sağlamak ve sanatsal değer sunmak gibi çeşitli amaçlarla kullanılabilir."}}

def tarihiEserler():
    global minyatürler # global minyatürler listesini kullanmak için burada belirttim
    print("minyatür seçiniz: 1- Ayasofya 2- Notre Dame Katedrali 3- Edinburg Kalesi")
    secim = int(input("bir seçim yapınız: ")) # kullanıcıdan seçim yapması isteniyor
    match secim:
        case 1:
            print(minyatürler[1])
        case 2:
            print(minyatürler[2])
        case 3:
            print(minyatürler[3])
        case _:
            print("Geçersiz seçim.")
    return

trhiTablolar = { # tarihi eserlerinin tablosu
    1: {"sanatkar": "Pablo Picasso", "tarihi": 1937, "aciklama": "Guernica: Guernica, Pablo Picasso tarafından 1937'de yapılan, İspanya İç Savaşı sırasında Nazi Almanyası'na ait 28 bombardıman uçağının 26 Nisan 1937'de İspanya'daki Guernica şehrini bombalamasını anlatan anıtsal tablodur."},
    2: {"sanatkar": "Velazquez", "tarihi": 1656, "aciklama": "Geç Orta Çağ İspanyası'nın en önemli ressamı sayılan Diego Velazquez'in 1656 tarihli tablosudur. Velazquez'in 1656 yılında yaptığı bu tablo, İspanyol sanatının örneklerindendir. Ayrıca, sanat tarihinin de ilk üç boyutlu tablosu olarak kabul edilir."},
    3: {"yazar": "Vincent van Gogh", "tarihi": 1889, "aciklama": "Yıldızlı Gece, Hollandalı art izlenimci ressam Vincent van Gogh tarafından yapılan yağlı boya tablo. Haziran 1889'da yaptığı tabloda ressam, sanatoryumdaki odasının doğuya bakan pencereden görünen Saint-Rémy-de-Provence köyünün gün doğuşundan hemen önceki görünüşünü resmetmiştir."}}

def tarihi_tablolari(): # tarihi tablolarını gösteren fonksiyon
    print("tablo seçiniz: 1- Guernica 2- Nedimeler 3- Yıldızlı Gece")
    secim = int(input("bir seçim yapınız: "))
    match secim: # kullanıcıdan seçim yapması isteniyor
        case 1:
            print(trhiTablolar[1])
        case 2:
            print(trhiTablolar[2])
        case 3:
            print(trhiTablolar[3])
        case _:
            print("Geçersiz seçim.")
    return

mezarEsyalari = { # mezar esyalarının listesi
    1: {"yazar": "Carter", "tarihi": 1925, "aciklama": "28 Ekim 1925 yılında keşfedilen Mısır'ın ölüm sonrası yaşam tanrısı Osiris'in suretini taşıyan bu maskenin omuzlarında hiyerogliflerle Ölüler Kitabından eski bir büyü yazılıdır"},
    2: {"yazar": "David Stuart Davies", "tarihi": None, "aciklama": ""},
    3: {"yazar": "", "tarihi": None, "aciklama": 
    "Canopic kavanozları, eski Mısır'da mezar kültürüyle ilişkilendirilen önemli sanat eserleridir. Bu kavanozlar, mumyalama işlemi sırasında kullanılan iç organların muhafaza edildiği kaplar olarak kullanılmıştır."}
       }

def antikMisirMezarEsyalari(): # antik Mısır mezar esyalarını gösteren fonksiyon    
    print("mezar eşyası seçiniz: 1- Tutankamunun Altın Maskesi 2- Ölüm Kitabi Papirüsü 3- Canopic Kavonazları")
    secim = int(input("bir seçim yapınız: "))
    match secim: # kullanıcıdan seçim yapması isteniyor
        case 1:
            print(mezarEsyalari[1])
        case 2:
            print(mezarEsyalari[2])
        case 3:
            print(mezarEsyalari[3])
        case _:
            print("Geçersiz seçim.")

def gorevli_ekle(): # gorevli ekleme fonksiyonu

    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    yasi = int(input("Yaş: "))
    kati = int(input("Kat: "))
    gorevli = {
        "isim": isim,
        "soyisim": soyisim,
        "yasi": yasi,
        "kati": kati
    }
    gorevliler.append(gorevli)

def katGorevlileri(): # kategoriye göre görevli listesini gösteren fonksiyon
    global gorevliler
    if len(gorevliler) == 0:
        print("Görevliler henüz eklenmemiş.")
        return
    kat = int(input("Hangi kattaki görevlilerin listesini görmek istersiniz: "))
    for gorevli in gorevliler:
        if gorevli["kati"] == kat:
            print(gorevli)
        else:
            print("Bu katta görevliler bulunmamaktadır.")

def degerlendirme(): # kullanıcı değerlendirmeleri listesini gösteren fonksiyon
    global kullanıcıDegerlendirmeleri
    degerlendirme = int(input("kaç yıldız veriyosunuz :) : "))
    kullanıcıDegerlendirmeleri = np.append(kullanıcıDegerlendirmeleri, degerlendirme)

def genelDegerlendirme(): # kullanıcıların genel değerlendirmelerini gösteren fonksiyon
    if kullanıcıDegerlendirmeleri.size > 0:
        genel_degerlendirme = np.mean(kullanıcıDegerlendirmeleri)
        print("Müzemizin genel yıldız puanı: ", genel_degerlendirme)
    else:
        print("Henüz değerlendirme yapılmamış.")

def kullanıcıKayıt(): # kullanıcı kayıt fonksiyonu
    global kullanıcıBilgileri # kullanıcı bilgilerini global listeye eklemek için burada belirttim
    kullanıcıAdı = input("kullanıcı adı giriniz: ") # kullanıcıdan bilgileri alıyoruz
    sifre = getpass.getpass("şifre giriniz: ")
    for kullanıcıBilgisi in kullanıcıBilgileri:
        if kullanıcıAdı == kullanıcıBilgisi["kullanıcıAdı"]:
            print("Bu kullanıcı adı zaten alınmış.")
            return
        if sifre == kullanıcıBilgisi["sifre"]:
            print("Bu şifre daha önceden alınmış.")
            return

    kayıtBilgisi = {
        "kullanıcıAdı": kullanıcıAdı,
        "sifre": sifre
    }
    kullanıcıBilgileri.append(kayıtBilgisi)
    print("Kullanıcı kaydı başarılı.")

def kullanıcıGirisi(): # kullanıcı giriş fonksiyonu
    kullanıcıAdı = input("kullanıcı adı giriniz: ")
    sifre = getpass.getpass("şifrenizi giriniz: ")
    for bilgiler in kullanıcıBilgileri:
        if kullanıcıAdı == bilgiler["kullanıcıAdı"] and sifre == bilgiler["sifre"]:
            print("giriş başarılı")
            return
    print("kullanıcı adı veya şifre yanlış :(") # kullanıcı adı veya şifre yanlış ise bu mesajı yazdırıyor

def yöneticiGirisi(): # yönetici giriş fonksiyonu
    kullanıcıAdı = input("kullanıcı adı giriniz: ")
    sifre = getpass.getpass("Şifre: ")
    # Yönetici giriş işlemleri burada yapılacak
    global yoneticiGBilgileri
    print("Yönetici girişi başarılı")
    if kullanıcıAdı == yoneticiGBilgileri[0] and sifre == yoneticiGBilgileri[1]:
        print("Yönetici İşlemleri")
        print("------------------")
        print("1. Görevli Ekle")
        print("2.Görevli Sil")
        print("3. Seminer Oluştur")
        print("4. Konferans Oluştur")
        print("5. Eğitim Programı Oluştur")
        secim = int(input("Yapmak istediğiniz Yönetici işlemini seçiniz: "))
        match secim:
            case 1:
                gorevli_ekle()
                print("Görevli başarıyla eklendi.")
            case 2:
                gorevliSil()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
            case 3:
                seminerOlustur()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
            case 4:
                konferansOlustur()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
            case 5:
                egitimProgramiOlustur()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
        return True
    else:
        print("Yanlış kullanıcı adı veya şifre.")
        return False
    return

sEserleri = { # sanat esyalarının listesi
    1: {
        "Geleneksel ve etnik çalgılar": "santoor, shamisen",
        "açıklama": "santoor, kökeni Hindistan, İran ve Orta Asya'ya dayanan, tahta bir çalgıdır. Santoor, ince telleri olan bir çalgı olup, tellere bir çekiçle vurarak çalınır. Bu çekiçler genellikle tahtadan yapılır ve her biri bir teli çalarak ses üretir. Shamisen, Japon kökenli geleneksel bir telli çalgıdır. Genellikle üç telli olan shamisen, genellikle Japonya'nın geleneksel müziği olan 'minyo' ve 'kabuki' tiyatrosu gibi performans sanatlarında kullanılır."
    },
    2: {
        "Modern ve deneysel çalgılar": "theremin,waterphone",
        "aciklama": "Theremin, elektronik bir müzik enstrümanıdır ve benzersiz bir özelliği vardır: Elle çalınmaz. Bu enstrüman, elektromanyetik alanlar aracılığıyla ellerin enstrümanın iki anteni arasındaki mesafeyi değiştirmesiyle ses üretir. Waterphone, suyun titreşimlerini kullanarak ses üreten deneysel bir müzik enstrümanıdır. Metal veya camdan yapılan bir gövdeye sahiptir ve çeşitli boyutlardaki çubuklarla çalınır."
    }
,
    3: {"tepelikler ve kil tabletleri": "Gılgamış Destanı,Hammurabi Kanunları, Asur tabletleri", "tarihi": "", "aciklama": "Gılgamış Destanı: Antik Mezopotamya'dan günümüze ulaşan en eski edebiyat eseri ve Piramit metinlerinden sonra en eski ikinci dini metin olarak kabul edilen destansı bir şiirdir. Yazım yılı M.Ö. 1800. Hammurabi Kanunları:bilindiği kadarıyla tarihin en eski ve en iyi korunmuş yazılı yasalarıdır. MÖ 1760 yılı civarında Mezopotamya'nın Babil ülkesinde ortaya çıkan kanunlar, Kral Hammurabi'nin çeşitli meselelerde verdiği kararları içerir. Hammurabi, kendisine bu yasaları yazdıranın Tanrı Şamaş olduğunu bildirir. Asur Tabletleri:Bu tabletler Yeni Asur devrine ait Anadolu'da bulunmuş en kapsamlı yasal belgelerdir ve 90 yıllık (MÖ 703- 613) bir tarih aralığına aittir. Yeni Asur çiviyazısı ve dilinde yazılmış tabletler arasında bir tane de Aramca etiket vardır."}
}

def sanatEserleri(): # sanat esyalarını gösteren fonksiyon
    print("sanat eseri kategorisi seçiniz: 1- Ses ve müzik 2- Geleneksel sanat eserleri 3- Dijital sanat eserleri")
    secim = int(input("bir seçim yapınız: "))
    match secim:
        case 1:
            print(sEserleri[1])
        case 2:
            print(sEserleri[2])
        case 3:
            print(sEserleri[3])
        case _:
            print("Geçersiz seçim.")

tarihler = [] # sanat eserleri tarihleri
none_tarihler = [] # tarihi belli olmayan eserler

minyatürler = { # minyatürlerin listesi
    1: {"yazar": "matrakçı nasuh", "tarihi": 1501, "aciklama": "Ayasofya minyatürü, Osmanlı minyatür sanatının ve İstanbul'un tarihi dokusunun önemli bir örneğidir. Sanatçı, bu minyatürde Ayasofya'nın mimari güzelliklerini ve tarihi önemini başarılı bir şekilde yansıtmıştır"},
    2: {"yazar": "anonim", "tarihi": 1301, "aciklama": "Notre Dame Katedrali'nin minyatürleri, genellikle Orta Çağ ve Rönesans dönemlerinde yapılmıştır. Minyatürler, Notre Dame Katedrali'nin mimari güzelliklerini ve tarihsel önemini vurgulayan değerli sanatsal eserlerdir."},
    3: {"yazar": "anonim", "tarihi": None, "aciklama": "Edinburgh Kalesi'nin minyatürü, kalenin mimarisini ve tarihini detaylı bir şekilde açıklamak, eğitim vermek, turistik bilgi sağlamak ve sanatsal değer sunmak gibi çeşitli amaçlarla kullanılabilir."}
}

def minyaturleriSirala(minyatürler):
    tarihler = [] 
    none_tarihler = []
    for value in minyatürler.values():
        if value['tarihi'] is not None:
            tarihler.append(value['tarihi'])
        else:
            none_tarihler.append(value['tarihi'])

    # None olmayan yani bilinmeyenler dışındaki tarihleri sırala
    tarihler.sort()

    #Sıralı tarihler listesi ve None tarih listesini birleştir
    sirali_tarihler = tarihler + none_tarihler

    #Sıralı tarihlere göre yeni bir sözlük oluştur
    sirali_minyatürler = {}
    for tarih in sirali_tarihler:
        for key, value in minyatürler.items():
            if value['tarihi'] == tarih:
                sirali_minyatürler[key] = value

    # Sıralı minyatürleri yazdır
    for key, value in sirali_minyatürler.items():
        print(f"ID: {key}, Yazar: {value['yazar']}, Tarihi: {value['tarihi']}, Açıklama: {value['aciklama']}")

def tablolarıSirala(trhiTablolar):
    tabloTarihleri = []
    none_tarihler = []

    # Verilen sözlüğü ayır ve tarihi olanları ve olmayanları ayrıştır
    for value in trhiTablolar.values():
        if value['tarihi'] is not None:
            tabloTarihleri.append(value['tarihi'])
        else:
            none_tarihler.append(value['tarihi'])

    # None olmayan tarihleri sırala
    tabloTarihleri.sort()

    # Sıralı tarihler listesi ve None tarih listesini birleştir
    sirali_tarihler = tabloTarihleri + none_tarihler

    # Sıralı tarihlere göre yeni bir sözlük oluştur
    siraliTablolar = {}
    for tarih in sirali_tarihler:
        for key, value in trhiTablolar.items():
            if value['tarihi'] == tarih and key not in siraliTablolar:
                siraliTablolar[key] = value

    # Sonuçları yazdır
    for key, value in siraliTablolar.items():
        yazar = value.get('yazar', 'Bilinmiyor')  # 'yazar' anahtarı yoksa 'Bilinmiyor' kullan
        aciklama = value.get('aciklama', 'Açıklama yok')  # 'aciklama' anahtarı yoksa 'Açıklama yok' kullan
        print(f"ID: {key}, Yazar: {yazar}, Tarihi: {value['tarihi']}, Açıklama: {aciklama}")


def kronoloji(): # kronoloji fonksiyonu eserleri kronolojik sıraya göre sıralar
    print("kronoloji bölümümüze hoşgeldiniz, gelin birlikte tarihin derinliklerine dalalım :)")
    print("Geçmişten günümüze kadar seçtiğiniz kategorideki eserleri inceleyin")
    print("1-minyatürler,2-tablolar")
    secim = int(input("zaman yolculuğu için bir kategori seçin: "))
    match secim:
        case 1:
            minyaturleriSirala(minyatürler)
        case 2:
            tablolarıSirala(trhiTablolar) 

def yorumBirak(): # müzeye yorum bırakma fonksiyonu
    global yorumVeritabani
    isim = input("isminizi giriniz: ")
    soyisim = input("soyisminizi giriniz: ")
    yorum = input("yorumunuzu giriniz: ")
    yBilgileri = { # kullanıcı bilgilerini bir sözlük olarak tanımladık
    "isim": isim,
    "soyisim": soyisim,
    "yorum": yorum
    }
    yorumVeritabani.append(yBilgileri) # kullanıcı bilgilerini yorum veritabanına ekliyoruz

def yorumlar():
    print(yorumVeritabani)

def ilgiTesti():  # kullanıcının hangi kategoride sanat eserine ilgi duyduğunu test eden fonksiyon
    print("Sanat eserlerine ilginizi belirlemek için birkaç soru soracağım. Lütfen aşağıdaki soruları yanıtlayınız.")

    # Sorular ve ilgi puanları
    sorular = {
        "Ses ve müzik": [
            {"soru": "Konserlere gitmeyi sever misiniz?", "cevap_tipi": "evet_hayir"},
            {"soru": "Enstrüman çalmayı veya öğrenmeyi düşündünüz mü?", "cevap_tipi": "evet_hayir"},
            {"soru": "Müzik festivallerine katılmaktan hoşlanır mısınız?", "cevap_tipi": "evet_hayir"}
        ],
        "Geleneksel sanat eserleri": [
            {"soru": "Müzelerde gezinmeyi sever misiniz?", "cevap_tipi": "evet_hayir"},
            {"soru": "Klasik resim veya heykel sanatına ilgi duyar mısınız?", "cevap_tipi": "evet_hayir"},
            {"soru": "Yerel sanat galerilerini ziyaret etmekten hoşlanır mısınız?", "cevap_tipi": "evet_hayir"}
        ],
        "Dijital sanat eserleri": [
            {"soru": "Sanal galerilere veya sanal gerçeklik sanat projelerine ilginiz var mı?", "cevap_tipi": "evet_hayir"},
            {"soru": "Dijital sanat eserlerini görmeyi veya oluşturmayı sever misiniz?", "cevap_tipi": "evet_hayir"},
            {"soru": "Dijital sanatla ilgili atölye çalışmalarına katılmayı düşünür müsünüz?", "cevap_tipi": "evet_hayir"}
        ]
    }

    # Kullanıcıya her kategorideki soruları sormak ve ilgi puanlarını hesaplamak
    ilgi_puanlari = {"Ses ve müzik": 0, "Geleneksel sanat eserleri": 0, "Dijital sanat eserleri": 0}

    # Soru sorma ve ilgi puanı hesaplama fonksiyonu
    def sorulari_sor_ve_puanla(kategori):
        for soru in sorular[kategori]:
            print(soru["soru"])

            if soru["cevap_tipi"] == "evet_hayir":
                cevap = str(input("(Evet/Hayır): ").strip().lower())
                while cevap not in ["evet", "hayır"]:
                    print("Lütfen sadece 'Evet' veya 'Hayır' şeklinde cevap verin.")
                    cevap = str(input("(Evet/Hayır): ").strip().lower())
                if cevap == "evet":
                    ilgi_puanlari[kategori] += 1

    # Kategorilere göre soruları otomatik olarak sırayla sor
    for kategori in sorular:
        sorulari_sor_ve_puanla(kategori)

    # En yüksek ilgi puanına sahip kategoriyi bul
    en_yuksek_ilgi = max(ilgi_puanlari, key=ilgi_puanlari.get)
    print(f"\nEn yüksek ilgi gösterdiğiniz kategori: {en_yuksek_ilgi}")

bgnSayisiMinyaturler = { # eserlerin beğeni sayısı
    1: {"isim": "Ayasofya", "begeni": 0},
    2: {"isim": "Notre Dame Katedrali", "begeni": 0},
    3: {"isim": "Edinburgh Kalesi", "begeni": 0}
}

bgnsayisitablolar = { # tabloların beğeni sayısı
    1: {"isim": "Guernica", "begeni": 0},
    2: {"isim": "Nedimeler", "begeni": 0},
    3: {"isim": "Yıldızlı Gece", "begeni": 0}
}

bgnSayisiMzrEsyalari = { # mezar eşyaları beğeni sayısı
    1: {"isim": "Tutankamunun Altın Maskesi", "begeni": 0},
    2: {"isim": "Ölüm Kitabi Papirüsü", "begeni": 0},
    3: {"isim": "Canopic Kavonazları", "begeni": 0}
}

eserler = { # eserler ve beğenileri listesi
    "minyaturler": bgnSayisiMinyaturler,
    "tablolar": bgnsayisitablolar,
    "mezar_Esyalari": bgnSayisiMzrEsyalari
}

def begeniBirak(): # beğeni bırakma fonksiyonu
    print("Minyatürler 1- Ayasofya 2- Notre Dame Katedrali 3- Edinburgh Kalesi")
    print("Tablolar 1- Guernica 2- Nedimeler 3- Yıldızlı Gece")
    print("Mezar taşları 1- Tutankamunun Altın Maskesi 2- Ölüm Kitabi Papirüsü 3- Canopic Kavonazları")
    print("Sanat eserleri 1- Ses ve müzik 2- Geleneksel sanat eserleri 3- Dijital sanat eserleri")

    eserBegeni = input("Beğendiğiniz eserin adını giriniz: ").strip().lower()
    eser_bulundu = False
    # eserlistesi içinde döngü yapıyoruz
    for kategori, eser_listesi in eserler.items():
        for eser in eser_listesi.values(): # eser_listesi içinde döngü yapıyoruz değerleri yani eserleri eser adlı değişkene atıyoruz
            if eser["isim"].lower() == eserBegeni:
                print("Eserimizi beğendiğinizi belirtmek için klavyenizden +1 girmelisiniz") # eğer kullanıcının girdiği eser listede varsa ekrana +1 yazısını yazıyoruz ve beğeni bırakıyoruz
                begeni = input().strip()
                if begeni == "+1":
                    eser["begeni"] += 1
                    print("Eserimizi beğendiğiniz için teşekkür ederiz, ayrıca sistemimizdeki ilgi testini çözerek ilginizin olduğu farklı tabloları da keşfedebilirsiniz :)")
                eser_bulundu = True
                break
        if eser_bulundu:
            break

    if not eser_bulundu:
        print("Girdiğiniz eser adı bulunamadı. Lütfen doğru bir eser adı girin.")

def begeniler(): # beğenileri gösterme fonksiyonu
        print("Beğeniler")
        for kategori, eser_listesi in eserler.items():
            print(f"\n{kategori.capitalize()}:")
            for eser in eser_listesi.values():
                print(f"{eser['isim']}: {eser['begeni']} beğeni")

def faveser(): # favori eseri gösteren fonksiyonu
    max_begeni = -1
    en_cok_begenilen_eser = None

    for eser_listesi in [bgnSayisiMinyaturler, bgnsayisitablolar, bgnSayisiMzrEsyalari]:
        for eser_id, eser in eser_listesi.items():
            if eser["begeni"] > max_begeni:
                max_begeni = eser["begeni"]
                en_cok_begenilen_eser = eser["isim"]

    if en_cok_begenilen_eser is not None:
        print(f"En çok beğenilen eser: {en_cok_begenilen_eser} - {max_begeni} beğeni")
    else:
        print("Henüz hiçbir eser beğenilmemiş.")

def gorevliSil(): # gorevli silme fonksiyonu
    global gorevliler
    grvlİsmi = input("silmek istediğiniz görevlinin ismini giriniz: ")
    grvlSoyismi = input("silmek istediğiniz görevlinin soyismini giriniz:")
    for gorevli in gorevliler:
        if gorevli["isim"] == grvlİsmi and gorevli["soyisim"] == grvlSoyismi:
                gorevliler.remove(gorevli)
                print(f"{grvlİsmi} {grvlSoyismi} adlı görevli başarıyla silindi.")
        else:
            print("Görevli bulunamadı.")

sergiler = { # sergiler listesi
    "Daimi Sergiler": {"Bilim ve teknoloji objeleri": "Teleskoplar,Astronomik saatler", "tarihi": "", "aciklama": ""},
    "Geçici Sergiler": {"Uzay keşfi: Apollo görevleri temalı": "Apollo 11'in iniş modülü modeli,Astronot Kıyafetleri,Aydan getirilen kaya örnekleri", "\nAntik mısır temalı": "Tutankhamun'un altın maskesi,Rosetta taşı,Antik mısır heykelleri", "aciklama": ""},
    "Tematik Sergiler": {"Empresyonizm Temalı": "Claude Monet Impression sunrise, Edgar Degas the Ballet Class", "\nRönesans Dönemi Temalı": "Leonardo Da Vinci: Mona Lisa,Raphael: The School of Athens", "aciklama": ""}
}

def sergiSınıflari(): # sergi sınıflarını gösteren fonksiyon
    print("1-Daimi Sergiler, 2-Geçici Sergiler, 3- Tematik Sergiler")
    secim = int(input("Bir seçim yapınız: "))
    match secim:
        case 1:
            print(sergiler["Daimi Sergiler"])
        case 2:
            print(sergiler["Geçici Sergiler"])
        case 3:
            print(sergiler["Tematik Sergiler"])
    return 

Programlar = { # programlar listesi
    1: {"adı": "Program 1", "tarihi": "01-01-2024", "konusu": "Konu 1", "saati": "10:00", "kayıtSayısı": 0, "kapasite": 150},
    2: {"adı": "Program 2", "tarihi": "02-01-2024", "konusu": "Konu 2", "saati": "11:00", "kayıtSayısı": 0, "kapasite": 100},
    3: {"adı": "Program 3", "tarihi": "03-01-2024", "konusu": "Konu 3", "saati": "12:00", "kayıtSayısı": 0, "kapasite": 200}
}

def egitimProgramlari(): # eğitim programlarını gösteren fonksiyon
    for program_id, program in Programlar.items():
        print(f"{program_id}: {program['adı']} - Tarih: {program['tarihi']}, Konu: {program['konusu']}, Saat: {program['saati']}, Kayıtlı Sayısı: {program['kayıtSayısı']}, Kapasite: {program['kapasite']}")

    secim = int(input("Katılmak istediğiniz eğitimi seçiniz : "))

    if secim in Programlar:
        secilen_program = Programlar[secim]
        print(f"Seçtiğiniz Program: {secilen_program}")

        if secilen_program["kayıtSayısı"] < secilen_program["kapasite"]:
            isim = input("İsminizi giriniz: ")
            soyisim = input("Soyisminizi giriniz: ")

            secilen_program["kayıtSayısı"] += 1
            print(f"Tebrikler {isim} {soyisim}! Kaydınız başarıyla tamamlandı.")
        else:
            print("Üzgünüz, bu eğitimin kapasitesi dolmuştur.")
    else:
        print("Geçersiz seçim.")

def egitimProgramiOlustur(): 
    # Kullanıcıdan eğitim programı bilgilerini alıyoruz.
    for i in range(1, 4):
        print(f"{i}. Program:")
        adi = input("Eğitim programının ismini giriniz: ")
        tarihi = input("Eğitim programının tarihini giriniz (YYYY-MM-DD): ")
        konusu = input("Eğitim programının konusunu giriniz: ")
        saati = input("Eğitim programının saatini giriniz (HH:MM): ")

        # Bilgileri sözlüğe yerleştiriyoruz.
        Programlar[i] = {
            "adı": adi,
            "tarihi": tarihi,
            "konusu": konusu,
            "saati": saati
        }

konferansListesi = {
    1: {"adı": "", "tarihi": "", "konusu": "", "saati": "", "kayıtSayısı": 0, "kapasitesi": 150},
    2: {"adı": "", "tarihi": "", "konusu": "", "saati": "", "kayıtSayısı": 0, "kapasitesi": 100},
    3: {"adı": "", "tarihi": "", "konusu": "", "saati": "", "kayıtSayısı": 0, "kapasitesi": 200}
}

def konferanslar():
    global konferansListesi
    for konferansKaydi in konferansListesi:
        print(konferansListesi[konferansKaydi])
    secim = int(input("Katılmak istediğiniz konferansı seçiniz: "))
    if secim in konferansListesi:
        if konferansListesi[secim]["kayıtSayısı"] < konferansListesi[secim]["kapasitesi"]:
            isim = input("İsminizi giriniz: ")
            soyisim = input("Soyisminizi giriniz: ")
            konferansListesi[secim]["kayıtSayısı"] += 1
            print(f"Tebrikler {isim} {soyisim}! Kaydınız başarıyla tamamlandı.")
        else:
            print("Üzgünüz, bu konferansın kapasitesi dolmuştur.")
    else:
        print("Geçersiz seçim.")

def konferansOlustur(): # konferans oluşturma fonksiyonu
    global konferansListesi
    konfIsmi = input("oluşturmak istediğiniz konferansın ismini giriniz: ")
    konfTarihi = input("oluşturmak istediğiniz konferansın tarihini giriniz: ")
    konfKonusu = input("oluşturmak istediğiniz konferansın konusunu girniz")
    konfSaati = input("oluşturmak istediğiniz konferansın saatini giriniz")
    konfKayitSayisi = 0
    konfKapasitesi = input("oluşturduğunuz konferansın kapasitesini belirleyiniz")

    konfBilgileri = {

        "adı": konfIsmi,
        "tarihi": konfTarihi,
        "konusu": konfKonusu,
        "saati": konfSaati,
        "kayıtSayısı": konfKayitSayisi,
        "kapasitesi": konfKapasitesi  
    }
    yeniId = max(konferansListesi.keys()) + 1  # Yeni konferansa bir ID verilir
    konferansListesi[yeniId] = konfBilgileri # yeni konferansa bilgileri eklenir
    print("Yeni konferans başarıyla oluşturuldu.")

seminerListesi = {
    1: {"ismi": "", "konusu": "", "tarihi": "","saati":"" ,"kayıtSayısı": 0,"kapasitesi":150},
    2: {"ismi": "", "konusu": "", "tarihi": "","saati":"","kayıtSayısı": 0,"kapasitesi":100},
    3: {"ismi": "", "konusu": "", "tarihi": "","saati":"","kayıtSayısı": 0,"kapasitesi":200}
}

def seminerler(): # seminerler listesini gösteren fonksiyon
    global seminerListesi
    for seminerKaydi in seminerListesi:
        print(seminerListesi[seminerKaydi])
    secim = int(input("Katılmak istediğiniz semineri seçiniz: "))
    if secim in seminerListesi:
        if seminerListesi[secim]["kayıtSayısı"] < seminerListesi[secim]["kapasitesi"]:
            seminerListesi[secim]["kayıtSayısı"] += 1
            print("Tebrikler! Kaydınız başarıyla tamamlandı.")
        else:
            print("Üzgünüz, bu seminerin kapasitesi dolmuştur.")
    else:
        print("Geçersiz seçim.")
    return

def seminerOlustur(): # seminer oluşturma fonksiyonu
    global seminerListesi
    semIsmi = input("oluşturmak istediğiniz konferansın ismini giriniz: ")
    semTarihi = input("oluşturmak istediğiniz konferansın tarihini giriniz: ")
    semKonusu = input("oluşturmak istediğiniz konferansın konusunu girniz")
    semSaati = input("oluşturmak istediğiniz konferansın saatini giriniz")
    semKayitSayisi = 0
    semKapasitesi = input("oluşturduğunuz konferansın kapasitesini belirleyiniz")
    semBilgileri = {
        "ismi": semIsmi,
        "konusu": semKonusu,
        "tarihi": semTarihi,
        "saati": semSaati,
        "kayıtSayısı": semKayitSayisi,
        "kapasitesi": semKapasitesi
    }
    yeniId = max(seminerListesi.keys()) + 1  # Yeni konferansa bir ID verilir
    seminerListesi[yeniId] = semBilgileri
    print("Yeni seminer kaydı oluşturuldu.")

def muzeHaritamiz(): # muze haritamızı gösteren fonksiyon
    global minyatürler,trhiTablolar,mezarEsyalari,sEserleri,sergiler,Programlar,konferansListesi,seminerListesi

    Katlar = {0: sergiler, 1: sEserleri, 2: trhiTablolar, 3: Programlar, 4: konferansListesi, 5: seminerListesi, 6: minyatürler, 7: trhiTablolar, 8: mezarEsyalari} # Kategorileri katlar sözlüğünde tutuyoruz
    print("Eserlerimizin genel olarak incelediniz, kat seçimi yaparak hangi katta hangi eserlerimiz var görebilir, müzemizde bir gezintiye çıkabilirsiniz :)")
    print("Müzemize Genel Bakış")
    print("--------------------")
    print("Müzemizdeki Katlari Gezebilirsiniz:")
    print("0-Sergiler, 1-Sanat Eserleri, 2-Tarihi Eserler, 3-Eğitim Programları, 4-Konferanslar, 5-Seminerler, 6-Minyatürler, 7-Tablolar, 8-Mezar Tasları")
    kat = input("Gitmek istediğiniz katı seçiniz: ") # Kullanıcıdan kat seçimi istiyoruz
    match kat: # katlara göre eserleri gösteriyoruz
        case "0":
            print(Katlar[0])
        case "1":
            print(Katlar[1])
        case "2":
            print(Katlar[2])
        case "3":
            print(Katlar[3])
        case "4":
            print(Katlar[4])
        case "5":
            print(Katlar[5])
        case "6":
            print(Katlar[6])
        case "7":
            print(Katlar[7])
        case "8":
            print(Katlar[8])

def projeyeGit(): # tarayıcıdan github sayfama yönlendirme
    url = "https://github.com/melikecaglar/muzeProjem/"
    webbrowser.open(url)

def main(): # müzemizin arayüzü
    while True:
        print("MÜZEMİZE HOŞGELDİNİZ")
        print("----------------------")
        print("1. Kullanıcı Kaydı")
        print("2. Kullanıcı Girişi")
        print("3. Yönetici Girişi")
        print("4. Tarihi Eser Minyatürleri")
        print("5. Tarihi Tablolar")
        print("6. Antik Mısır Mezar Taşları")
        print("7. Görevli Ekle")
        print("8. Görevli Sil")
        print("9. Kat Görevlileri")
        print("10. Değerlendirme")
        print("11. Genel Değerlendirme")
        print("12. Eğitim Programı Oluşturma")
        print("13. Eğitim Programlarına Katılma")
        print("14. Konferansa Katıl")
        print("15. Konferans Oluştur")
        print("16. Seminere Katıl")
        print("17. Seminer Oluştur")
        print("18. Yorum yap")
        print("19. Yorumlar")
        print("20. İlgi alanınızı keşfedin :)")
        print("21. Beğeni bırakın")
        print("22. Beğeniler")
        print("23. Favori Eser")
        print("24. Zaman Yolculuğu")
        print("25. Müze Haritamız")
        print("26. Sanal Müzemizi Geliştirmek ister misiniz :) ")
        print("0. Çıkış")
        secim = int(input("Bir seçim yapınız: "))
        match secim:
            case 1:
                kullanıcıKayıt()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ") # kullanıcıya devam etmek isteyip istemediğini soruyoruz
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 2:
                kullanıcıGirisi()  
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 3:
                yöneticiGirisi()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 4:
                tarihiEserler()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 5:
                tarihi_tablolari()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 6:
                antikMisirMezarEsyalari()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 7:
                if yöneticiGirisi():
                    yöneticiGirisi()
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
                else:
                    print("Yönetici girişi başarısız.")
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
            case 8:
                if yöneticiGirisi():
                    yöneticiGirisi()
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
                else:
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
            case 9:
                katGorevlileri()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 10:
                degerlendirme()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 11:
                genelDegerlendirme()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 12:
                if yöneticiGirisi(): 
                    yöneticiGirisi()
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
                else:
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
            case 13:
                egitimProgramlari()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 14:
                konferanslar()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 15:
                if yöneticiGirisi():
                    yöneticiGirisi()
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
                else:
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
            case 16:
                seminerler()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 17:
                if yöneticiGirisi():
                    yöneticiGirisi()
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
                else:
                    secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                    if secenek.lower() == "evet":
                        main()
                    else:
                        print("Teşekkürler, iyi günler dileriz.")
                        break
            case 18:
                yorumBirak()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 19:
                yorumlar()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 20:
                ilgiTesti()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 21:
                begeniBirak()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 22:
                begeniler()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 23:
                faveser()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 24:
                kronoloji()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 25:
                muzeHaritamiz()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 26:
                projeyeGit()
                secenek = input("Uygulamamızı kullanmaya devam etmek ister misiniz? (Evet/Hayır): ")
                if secenek.lower() == "evet":
                    main()
                else:
                    print("Teşekkürler, iyi günler dileriz.")
                    break
            case 0:
                print("Çıkış yapılıyor...")
                break      
            case _:
                print("Geçersiz seçim.")

if __name__ == "__main__":
    main()

