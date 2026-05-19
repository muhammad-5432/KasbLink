📝 KasbLink — Tech Spec (v2.0)

### 1. Project Idea (Loyiha g‘oyasi)

KasbLink — bu santexnik, usta, elektrik kabi qisqa muddatli va kunlik ishlar qiluvchi offline freelancelar (Worker) uchun buyurtma topish, hamda usta qidirayotgan mijozlar (Client) uchun o‘z hududiga yaqin mutaxassislarni ularning real tajribasi, ijtimoiy postlari va reytingiga qarab topishga mo‘ljallangan minimalistik platforma. Ilova interfeysi va navigatsiyasi Instagram mantiqiga asoslanadi.

### 2. User Roles & Privacy (Rollari va Maxfiylik)

- **Client (Mijoz):** Ish e’loni beradi yoki usta qidiradi. Profil mutlaqo Yopiq (Private). Hech kim uning sahifasiga kira olmaydi. Sharhlar tarixida faqat ismi va familiyasining birinchi harfi ko‘rinadi (Asrorbek O.). Aniq lokatsiyasi faqat usta bilan kelishilgandan keyin chatda yuboriladi.
    
- **Worker (Usta):** O‘z xizmatlarini joylaydi, mijozlar e’loniga taklif yuboradi. Profil Ochiq (Public). Ismi, rasmi, mutaxassisligi, reytingi va postlari hamma uchun ko‘rinadi. Worker baribir tizim uchun "User" hisoblanadi (shuning uchun u boshqa workerlarning xizmatlaridan foydalana oladi).
    
- **Admin:** Tizim boshqaruvi, foydalanuvchilar bazasi va shubhali reytinglarni moderatsiya qilish.
    

### 3. Minimalistik Sahifalar Tuzilishi (Instagram-style Navigation)

Ilovaning pastki qismida jami 4 ta asosiy sahifa (Tab) bo‘ladi. Foydalanuvchining roliga ko‘ra (Client yoki Worker) sahifalar mazmuni avtomatik o‘zgaradi:

📱 **1-Sahifa: Main Feed (Asosiy Lenta)** E’lonlar yonma-yon emas, tepadan pastga (Single Column Feed) formatida joylashadi. Ikki xil e’lon aralashib ketmaydi:

- **Client uchun (Service List):** Ustalar xizmatlari e’loni chiqadi. Tepada aniq filtrlar (Kategoriya, reyting) bo‘ladi. E’londa ustaning kichik rasmi, ismi, reytingi, xizmat tavsifi (~75 so‘z) va min-max narxi ko‘rinadi. Sana/vaqt yo‘q.
    
- **Worker uchun (Job Board & Service List):**
    
    - **Job Board:** Mijozlar qoldirgan ish e’lonlari chiqadi. E’londa: qilinishi kerak bo‘lgan ish tavsifi, budjet va ish bajarilishi kerak bo‘lgan sana va vaqt (majburiy) ko‘rinadi.
        
    - **Service List:** Worker boshqa workerlarning xizmatlaridan foydalana oladi, ya'ni u xuddi mijoz kabi boshqa ustalarning xizmatlari ro‘yxatini ko‘ra oladi.
        
    - **Filtrlar:** Kasblar bo‘yicha (Default: Workerning o‘z kasblari bo‘yicha filterlangan turadi, lekin o‘zi o‘zgartira oladi), min-max narx bo‘yicha, lokatsiya bo‘yicha (tuman yoki shahar bo‘yicha, default workerning regioni va tumani bo‘yicha).
        

📱 **2-Sahifa: Explore Feed (Kashfiyot / Ijtimoiy Lenta)** Xuddi Instagram kabi, ustalarning portfolio va ish jarayonlari rasmlari/videolari turadigan ijtimoiy sahifa. Bu yerda **Grid (eniga va bo‘yiga multiple)** format ishlatiladi (Hech qanday Reels bo‘lmaydi, faqat klassik postlar).

- Mantiq: Mijoz o‘z hududidagi ustalarning qilgan ishlarini vizual ko‘rib, post tagidagi "Bog'lanish" tugmasi orqali to‘g‘ridan-to‘g‘ri usta bilan chatga o‘tishi mumkin. Postlarga Like bosish va Comment yozish mumkin.
    

📱 **3-Sahifa: Chat & Orders (Aloqa bo‘limi)** Mijoz va usta o‘rtasidagi barcha yozishmalar va joriy buyurtma statuslari jamlanadigan yagona oyna. Ortiqcha sahifalarni kamaytirish uchun chat va buyurtma jarayoni shu yerning o‘zida boshqariladi.

📱 **4-Sahifa: Profile (Profil sahifasi)**

- **Client Profil (Yopiq):** Faqat o‘zining sozlamalari, "Sevimlilar" (Favourites) ro‘yxati va "Mening buyurtmalarim tarixi" (o‘zi ko‘rishi uchun) joylashadi.
    
- **Worker Profil (Ochiq):** Ustaning bosh sahifasi. Tepada: rasm, ism, bio, hudud va reyting (Rating). Pastki qismida 2 ta ustun (Tab) bo‘ladi:
    
    - **Postlar (Grid):** Ustaning o‘zi yuklagan ijtimoiy postlari, foydali maslahatlari va rasmlari (Instagram profili kabi, multiple grid).
        
    - **Bajarilgan ishlar (List):** Faqat KasbLink orqali muvaffaqiyatli bitgan real buyurtmalar xronologiyasi. Bu yerda mijoz yozgan sharh, qo‘ygan yulduzchasi va ish rasmi o‘chirilmaydigan hujjat bo‘lib turadi.
        

### 4. Trust & Rating System (Ishonch tizimi)

Yangi usta himoyasi: Dastlabki 5 ta sharh (review) yig‘ilguncha ustaning o‘rtacha reyting raqami ko‘rsatilmaydi, o‘rniga "Yangi usta" (New) nishoni turadi. 5 ta sharhdan keyin o‘rtacha ball (⭐ 4.8) ochiladi.

### 5. Booking & Order System (Buyurtmalar mantiqi)

- Mijoz ustaga so‘rov yuborganda: Chat yoki tel orqali kelishilgach, mijoz usta e’lonidagi "So‘rov yuborish" tugmasini bosadi. Status: Kutilmoqda. Usta tasdiqlasa -> Jarayonda.
    
- Usta mijoz e’loniga taklif berganda: Usta e’lonni ko‘rib chatga kiradi va taklif yuboradi (Kunlik limit: 10-15 ta taklif). Mijoz qabul qilsa, unga aniq lokatsiya ochiladi va status -> Jarayonda bo‘ladi.
    
- Statuslar: Kutilmoqda (Pending) ➔ Jarayonda (In Progress) ➔ Bajarildi (Completed) yoki Rad etildi (Cancelled — faqat boshlanishidan oldin, izoh ixtiyoriy, e'lon o'chadi).
    

### 6. Review & Job Completion (Ishni tezkor yakunlash)

Ish Bajarildi bo‘lgach, jarayon "jaydari" va tez o‘tishi uchun tizim quyidagicha ishlaydi:

- **Worker uchun:** Matn yozmaydi, tayyor teglarni tanlaydi (Masalan: #krantuzatish, #gofra). Rasm yuklash ixtiyoriy. Bir tugma bilan buni Explore Feedga post qilib yuborishi ham mumkin.
    
- **Client uchun (Majburiy):** 1 dan 5 gacha yulduzcha tanlaydi va tayyor fikr-teglarni bosadi (Masalan: [xf] Tez keldi, [xf] Sifatli ish). Matnli izoh yozish esa ixtiyoriy.
    

### 7. Database Schema (Asosiy Jadvallar Kontsepti)

- **User** (id, phone, password, role, region_id, district_id, created_at)
    
- **WorkerProfile** (id, user_id, bio, overall_rating, review_count, region, district, location_geo)
    
- **Service** (id, worker_id, category_id, description, min_price, max_price)
    
- **Category** (id, name_uz, icon)
    
- **Order** (id, client_id, worker_id, service_id, status, scheduled_at, price, location_snapshot)
    
- **Post** (id, worker_id, order_id_is_verified, media_url, content, likes_count, created_at)
    
- **Comment** (id, post_id, user_id, content, created_at)
    
- **Like** (id, post_id, user_id)
    
- **Review** (id, order_id, client_id, worker_id, rating, tags, comment, created_at)
    
- **Favorite** (id, client_id, worker_id)
    
- **Message** (id, chat_id, sender_id, text, location_geo, created_at)
