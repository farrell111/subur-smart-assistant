import streamlit as st
import pandas as pd
import time
import os

# --- FUNGSI UNTUK MEMBUAT DATA DUMMY OTOMATIS ---
def init_dummy_data():
    if not os.path.exists("troubleshooting_data.csv"):
        kb_data = {
            "Kategori": ["CCTV", "CCTV", "CCTV", "CCTV", "CCTV", "Komputer", "Komputer", "Komputer", "Komputer", "Jaringan"],
            "Masalah": ["DVR bunyi bip panjang terus-menerus", "Layar monitor CCTV blank hitam (No Video)", "CCTV offline tidak bisa dilihat di HP", "Kamera CCTV buram atau berembun di malam hari", "Rekaman CCTV hilang atau tidak tersimpan (Playback kosong)", "PC menyala tapi monitor No Display", "Laptop tiba-tiba blue screen (BSOD) saat main game", "Kinerja PC sangat lambat dan lemot (Disk 100%)", "Bunyi kipas prosesor sangat berisik dan PC panas", "Internet putus nyambung di router (RTO)"],
            "Keywords": ["bunyi bip panjang dvr berisik alarm", "layar monitor mati blank hitam no video gelap", "offline hp handphone internet luar aplikasi pantau", "buram embun malam kabut kotor tidak jelas", "rekaman hilang kesave save tersimpan playback kosong memori memory hdd hardisk", "pc nyala monitor mati no display vga", "blue screen bsod restart sendiri game", "lambat lemot patah patah disk 100% lelet", "berisik kipas fan panas overheat", "internet putus rto nyambung wifi router"],
            "Penyebab_Umum": ["Hard Disk (HDD) tidak terbaca, rusak, atau adaptor daya kurang tegangan.", "Kabel coaxial/LAN putus, konektor BNC kendor, atau adaptor kamera mati.", "DVR tidak terkoneksi ke internet, kabel LAN rusak, atau status Cloud Offline.", "Kaca lensa kotor, embun terjebak di dalam housing, atau pantulan inframerah.", "Hard disk penuh dan tidak auto-overwrite, pengaturan jadwal rekam salah, atau HDD rusak.", "RAM kotor/longgar, atau kabel VGA/HDMI ke monitor bermasalah.", "Suhu terlalu panas (Overheating), driver VGA crash, atau RAM bermasalah.", "Hard disk mekanik sudah lemah, banyak virus, atau update Windows tersangkut.", "Thermal paste kering, debu menumpuk di heatsink, atau kipas rusak.", "Kabel fiber optik tertekuk, router panas, atau gangguan dari ISP."],
            "Solusi_Langkah": [
                "1. Matikan DVR.\n2. Buka casing dan pastikan kabel daya & SATA Hard Disk terpasang rapat.\n3. Jika masih bip, coba ganti adaptor DVR.\n4. Masuk ke menu Storage/HDD, cek apakah statusnya 'Uninitialized', lalu format jika perlu.",
                "1. Periksa apakah lampu inframerah kamera menyala saat ditutup tangan.\n2. Cek colokan BNC di belakang DVR dan di kamera.\n3. Ganti port channel di DVR untuk memastikan port tidak rusak.",
                "1. Pastikan kabel LAN dari router ke DVR terpasang kencang.\n2. Masuk ke menu Network di DVR, pastikan DHCP 'Enable'.\n3. Buka menu Platform Access / Cloud, pastikan statusnya 'Online'.",
                "1. Bersihkan kaca luar kamera dengan kain microfiber.\n2. Jika berembun di dalam, buka cover kamera dan keringkan.\n3. Pastikan tidak ada benda yang terlalu dekat di depan kamera agar inframerah tidak memantul.",
                "1. Masuk ke menu HDD/Storage di DVR, pastikan HDD berstatus 'Normal'.\n2. Cek menu Record Schedule, pastikan jadwal rekaman penuh 24 jam.\n3. Aktifkan fitur 'Overwrite' agar rekaman lama otomatis terhapus.",
                "1. Matikan PC dan cabut kabel power.\n2. Cabut RAM, gosok perlahan pin kuningnya menggunakan penghapus.\n3. Pasang kembali hingga bunyi 'klik'.\n4. Pastikan kabel monitor dicolok ke VGA Card (jika ada), bukan ke Motherboard.",
                "1. Catat kode error yang muncul (misal: VIDEO_TDR_FAILURE).\n2. Bersihkan ventilasi udara laptop agar sirkulasi lancar.\n3. Update driver kartu grafis ke versi terbaru.\n4. Gunakan cooling pad saat bermain game.",
                "1. Upgrade Hard Disk (HDD) lawas Anda ke SSD untuk kecepatan 10x lipat.\n2. Buka Task Manager (Ctrl+Shift+Esc), cek aplikasi apa yang memakan disk 100%.\n3. Matikan program startup yang tidak perlu.",
                "1. Matikan PC dan bersihkan debu pada kipas prosesor.\n2. Buka heatsink dan oleskan thermal paste baru pada prosesor.\n3. Pastikan kabel kipas terpasang ke pin 'CPU_FAN' di Motherboard.",
                "1. Restart router dengan mencabut adaptor listrik selama 1 menit.\n2. Pastikan kabel optik kuning tidak tertekuk tajam.\n3. Jika lampu PON berkedip merah/mati, hubungi teknisi ISP."
            ]
        }
        pd.DataFrame(kb_data).to_csv("troubleshooting_data.csv", index=False)

    if not os.path.exists("analytics_dummy.csv"):
        analytics_data = {
            "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Ags", "Sep"],
            "Keluhan_CCTV": [45, 52, 38, 60, 48, 55, 62, 50, 42],
            "Keluhan_Komputer": [30, 28, 35, 32, 40, 38, 45, 42, 30],
            "Keluhan_Jaringan": [10, 15, 12, 18, 14, 20, 16, 12, 8]
        }
        pd.DataFrame(analytics_data).to_csv("analytics_dummy.csv", index=False)

# Jalankan pembuatan data
init_dummy_data()

# --- SETUP HALAMAN ---
st.set_page_config(page_title="Subur Smart Assistant", page_icon="🏢", layout="wide")

@st.cache_data
def load_kb():
    return pd.read_csv("troubleshooting_data.csv")

@st.cache_data
def load_analytics():
    return pd.read_csv("analytics_dummy.csv")

df_kb = load_kb()
df_analytics = load_analytics()

# --- HEADER & BRANDING ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830312.png", width=80)
with col2:
    st.title("SUBUR CCTV & KOMPUTER")
    st.markdown("**Sistem Manajemen Terpadu: AI Support & Analytics Dashboard**")

st.divider()

tab1, tab2, tab3 = st.tabs(["💬 AI Support Chat", "📊 Data Analytics", "⚙️ Knowledge Base Admin"])

# ==========================================
# TAB 1: CHAT INTERFACE 
# ==========================================
with tab1:
    st.subheader("🤖 Asisten Teknisi Virtual")
    st.caption("AI ini dilatih menggunakan manual teknis untuk memandu pelanggan melakukan perbaikan mandiri.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Halo! Saya Asisten AI dari **Subur CCTV & Komputer**. Apakah ada kendala pada CCTV, Komputer, atau Jaringan Anda hari ini?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ketik keluhan Anda (misal: 'rekaman cctv ga kesave' atau 'pc bunyi berisik')..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Menganalisis masalah dari database teknis..."):
                time.sleep(1.0)
                
                # --- LOGIKA PENCARIAN BARU (SCORING SYSTEM) ---
                user_words = prompt.lower().split()
                best_match = None
                highest_score = 0
                
                for index, row in df_kb.iterrows():
                    # Gabungkan teks masalah dan keywords tersembunyi
                    search_text = str(row.get('Keywords', '')) + " " + row['Masalah']
                    search_text = search_text.lower()
                    
                    score = 0
                    for word in user_words:
                        if len(word) > 2 and word in search_text:
                            score += 1
                            if word in ['rekaman', 'kesave', 'bunyi', 'mati', 'lambat', 'berisik', 'offline']:
                                score += 2 
                            
                    if score > highest_score:
                        highest_score = score
                        best_match = row
                
                if best_match is not None and highest_score >= 1:
                    response_text = f"**Berdasarkan keluhan Anda, ini identifikasi masalahnya:**\n{best_match['Masalah']}\n\n"
                    response_text += f"**Kemungkinan Penyebab:**\n{best_match['Penyebab_Umum']}\n\n"
                    response_text += "**🔧 Langkah Perbaikan yang Bisa Anda Lakukan:**\n"
                    response_text += best_match['Solusi_Langkah']
                else:
                    response_text = "Mohon maaf, keluhan Anda tidak terdeteksi dengan jelas di database saya. Apakah bisa dijelaskan lebih detail masalahnya? (Misal: apakah ada pesan error di layar, atau bunyi tertentu?)"

                def stream_data():
                    for word in response_text.split(" "):
                        yield word + " "
                        time.sleep(0.02)
                
                st.write_stream(stream_data)
        
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# ==========================================
# TAB 2: DATA ANALYTICS DASHBOARD
# ==========================================
with tab2:
    st.subheader("📈 Trend Keluhan Pelanggan (2026)")
    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric(label="Total Tiket Servis", value="752", delta="+12% bulan ini")
    col_b.metric(label="Masalah CCTV Terbanyak", value="No Video / Blank", delta="-5% dari bulan lalu", delta_color="inverse")
    col_c.metric(label="Resolusi Mandiri via AI", value="68%", delta="Naik 15%")
    col_d.metric(label="Rata-rata Waktu Respons", value="2 Detik", delta="Stabil")
    
    st.markdown("---")
    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.markdown("**Tren Volume Keluhan per Kategori**")
        st.line_chart(df_analytics.set_index('Bulan'))
    with chart_col2:
        st.markdown("**Persentase Kategori Masalah**")
        total_cctv = df_analytics['Keluhan_CCTV'].sum()
        total_komputer = df_analytics['Keluhan_Komputer'].sum()
        total_jaringan = df_analytics['Keluhan_Jaringan'].sum()
        df_summary = pd.DataFrame({
            'Kategori': ['CCTV', 'Komputer', 'Jaringan'],
            'Total Keluhan': [total_cctv, total_komputer, total_jaringan]
        })
        st.bar_chart(df_summary.set_index('Kategori'), color="#FF4B4B")

# ==========================================
# TAB 3: ADMIN KNOWLEDGE BASE
# ==========================================
with tab3:
    st.subheader("⚙️ Manajemen Database Solusi")
    st.markdown("Halaman ini khusus untuk admin/teknisi menambahkan masalah dan solusi baru agar AI semakin pintar.")
    # Menampilkan tabel tanpa kolom 'Keywords' agar antarmuka admin rapi
    st.dataframe(df_kb[['Kategori', 'Masalah', 'Penyebab_Umum', 'Solusi_Langkah']], use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 | Portofolio by Farrell Engelbert")