import streamlit as st
import base64

# -----------------------------
# ✅ MUST BE FIRST Streamlit call
# -----------------------------
st.set_page_config(page_title="91 Care Pharma Helpdesk", page_icon="🏥")

# -----------------------------
# Background & Button Styles
# -----------------------------
def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

img = get_base64("bg.jpeg")

if img:
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)),
                    url("data:image/jpeg;base64,{img}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)



st.markdown("""
<style>
div.stButton > button {
    background-color: #f0f2f6;
    color: black;
    border-radius: 8px;
    height: 45px;
}
div.stButton > button:hover {
    background-color: #007bFF;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Session State
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = "greeting"

if "role" not in st.session_state:
    st.session_state.role = None


# -----------------------------
# Reusable Back Button
# -----------------------------
def back_to_main():
    if st.button("⬅ Back"):
        st.session_state.step = "main"


# -----------------------------
# Greeting Section
# -----------------------------
def greeting():
    st.subheader("Welcome to 91 Care IPD Helpdesk")
    st.write("**Your Role please:**")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👨‍⚕️pharmacist "):
            st.session_state.role = "pharmacis"
            st.session_state.step = "main"  

    

    with col2:
        if st.button("🧑‍💻Admin"):
            st.session_state.role = "Admin"
            st.session_state.step = "main"


# -----------------------------
# Role-Based Main Menu
# -----------------------------
def main_menu():
    role = st.session_state.role

    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🔙"):
            st.session_state.role = None
            st.session_state.step = "greeting"

    st.subheader(f"Hello {role}, How can I help you?")



    if role == "pharmacis":
        col1, col2, col3 = st.columns(3)            
        with col1: 
            if st.button("💵New Bill"):
                st.session_state.step = "New_Bill"
        with col2:    
            if st.button("📦Add stock"):
                st.session_state.step = "Add_stock"
        with col3:        
            if st.button("📦Modify stock"):
                st.session_state.step = "Modify_stock"
        col1, col2, col3 = st.columns(3)
        with col1:            
            if st.button("💳Billing"):
                st.session_state.step = "Billing" 
        with col2:              
            if st.button("📦Indent Management"):
                st.session_state.step = "Indent_Management"
        with col3:                
            if st.button("↔️Store Transfer"):
                st.session_state.step = "Store_Transfer"
        col1, col2, col3 = st.columns(3)
        with col1:           
            if st.button("💊Medicine"):
                st.session_state.step = "Medicine"
        with col2:        
            if st.button("💻Issue Medication Via Online Rx"):
                st.session_state.step =  "Online_Prescription"         

        
       

    elif role == "Admin":
        col1, col2, col3 = st.columns(3)            
        with col1: 
            if st.button("💵New Bill"):
                st.session_state.step = "New_Bill"
        with col2:    
            if st.button("📦Add stock"):
                st.session_state.step = "Add_stock"
        with col3:        
            if st.button("📦Modify stock"):
                st.session_state.step = "Modify_stock"
        col1, col2, col3 = st.columns(3)
        with col1:            
            if st.button("💳Billing"):
                st.session_state.step = "Billing" 
        with col2:              
            if st.button("📦Indent Management"):
                st.session_state.step = "Indent_Management"
        with col3:                
            if st.button("↔️Store Transfer"):
                st.session_state.step = "Store_Transfer"
        col1, col2, col3 = st.columns(3)
        with col1:           
            if st.button("💊Medicine"):
                st.session_state.step = "Medicine"
        with col2:        
            if st.button("💻Issue Medication Via Online Rx"):
                st.session_state.step =  "Online_Prescription"         

        

# -----------------------------
# Logo Header (safe — after set_page_config)
# -----------------------------
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    colA, colB = st.columns([1, 3])
    with colA:
        try:
            st.image("loginlogo.jpg", width=70)
        except Exception:
            st.markdown("🏥")
    with colB:
        st.markdown("<h2 style='margin-top:15px;'>91 Care</h2>", unsafe_allow_html=True)


# -----------------------------
# Feature Pages
# -----------------------------
def New_Bill():
    st.markdown("""
### 💊 Generate Pharmacy Bill Instructions

🔹 Go to the **Pharma Tab**  
🔹 On the **Dashboard Page**, locate the **New Bill** button at the top right  
🔹 Click on **New Bill** to create a new bill  
🔹 Enter the **Medicine Name**, **Quantity**, and **Discount**  
🔹 After entering details, you can:  
&nbsp;&nbsp;&nbsp;&nbsp;✔️ Save the bill  
&nbsp;&nbsp;&nbsp;&nbsp;🗑️ Delete the bill  
&nbsp;&nbsp;&nbsp;&nbsp;💳 Pay the bill  
🔹 Use the buttons available at the bottom of the page to complete the action  
""")
    back_to_main()

def Add_stock():
    st.markdown("""
### 📦 Stock Management Instructions

🔹 Go to the **Dashboard**  
🔹 Click on the **Add Stock** button at the top right  

🔹 You will see two options:  
    • **Add Stock** – Use this to update stock for existing items  
    • **Add New Stock** – Use this to add a completely new item  

🔹 Select the required option  
🔹 Fill in all the necessary fields on the page  
🔹 Click **Save** to add or update the stock  
""") 
    back_to_main() 


def Modify_stock():
    st.markdown("""
### 📦 Stock Management Instructions

🔹 Go to the **Dashboard**  
🔹 You will see the list of all stock items  

🔹 At the end of each row, you will find three buttons along with **Expiry date**:   
    • **View Stock** – View detailed information of the stock  
    • **Edit Stock** – Modify the stock details            
    • **Delete Stock** – Remove the stock from the list  

🔹 Click the required button to perform the desired action  
""")
    back_to_main()



def Billing():
    st.markdown("""
### 💳 Billing Instructions

🔹 Go to the **Billing** section  
🔹 View the list of bills based on date  
🔹 At the end of each row, you will find the following options:  
 1️⃣ **Pay Invoice**  
    → Used to view or complete payment for the bill  

 2️⃣ **Return Invoice**  
    → Used to generate a return bill  

 3️⃣ **View PDF**  
    → Used to see the bill in PDF format and print it  

 4️⃣ **Prescription**  
    → Used to view the PDF of prescribed medicines and patient details  

""")
    back_to_main()



def Indent_Management():
    st.markdown("""
### 📦 Indent Management Instructions  
🔹 Go to the **Pharmacy Indent** Page 
🔹 Fill in all the required details   
🔹 Click on the **Add Item** button    

✅ The indent will be added successfully  
🔹 Go to the **Indent Management** page  
🔹 Select the **Store**  
🔹 Choose the **Date**  

🔹 Based on your selection, you can view:  
    • 📋 **Indent Item Details**  
    • 🕒 **Indent History**  
    • 📍 **Indent Tracking**

🔹 Only Authorised users can  **Approves the Indent** .                

✅ This helps you monitor and manage indent activities efficiently
""")
    back_to_main()


def Store_Transfer():
    st.markdown("""
### 🔄 Store Transfer Instructions 
                
🔹 Go to the **Stores** section    
🔹 You can view the list of all available stores    

🔹 At the end of each row:    
    • Click the **Edit (✏️) icon** to modify the store name   

🔹 At the top right corner:    
    • Click on **Add Store** to create a new store    
    • Enter the required details and save              

🔹 Go to the **Store Transfer** page    
🔹 At the top right, you will find **Store Transfer** and **Download** buttons    
🔹 Click on **Store Transfer**    
🔹 Fill in the required details:  
    - From Store   
    - To Store    
    - Select Medicine    

🔹 Click on **Add Store** to complete the transfer    
🔹 Use the **Download** button to download the Store Transfer report   
    """)
    back_to_main()


def Medicine():
    st.markdown("""
### 💊 Medicine Management Instructions  

🔹 Go to the **Medicine** page    
🔹 You can see the **list of medicines**    
🔹 At the end of each row:  
 • Click the **Edit (✏️) icon** to update medicine details  

🔹 At the top right:  
 • Click the **Add Medicine** button  
 • Fill in the required details  
 • Click **Save/Add** to add a new medicine       
""")
    back_to_main()

def Online_Prescription(): 
    st.markdown("""
### 💊 Issue by Online RX Instructions  

🔹 Go to the **Issue by Online RX** page    
🔹 You will see the **list of prescriptions**      
 • Medicines prescribed by the doctor in OPD will appear here    

🔹 Click on a prescription to view details    
🔹 The pharmacist should:   
 • Enter the **issued quantity**  
 • Click on **Submit** to complete the process  
""")
    back_to_main()

# -----------------------------
# Navigation Controller
# -----------------------------
step = st.session_state.step

if step == "greeting":
    greeting()
elif step == "main":
    main_menu()
elif step == "New_Bill":
    New_Bill()
elif step == "Add_stock":
    Add_stock()
elif step == "Modify_stock":
    Modify_stock()
elif step == "Billing":
    Billing()
elif step == "Indent_Management":
    Indent_Management() 
elif step == "Store_Transfer":
    Store_Transfer()  
elif step =="Medicine":
    Medicine()
elif step ==  "Online_Prescription":
    Online_Prescription()    

