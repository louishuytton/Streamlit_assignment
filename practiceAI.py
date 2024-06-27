import streamlit as st

st.header("Trà Sữa CoTAI")

col_1, col_2 = st.columns(2)
with col_1:
    st.image("https://imgur.com/lEpdPsT.png")

with col_2:
    size = st.radio("Kích cỡ ", ("Nhỏ (30K)", "Vừa (40K)", "Lớn (50K)"), horizontal = True)
    st.write("Thêm")
    col1, col2 = st.columns(2)
    with col1:
        add_1 = st.checkbox("Sữa (5K)")
        add_2 = st.checkbox("Cà phê (8K)")
    with col2:
        add_3 = st.checkbox("Kem (10K)")
        add_4 = st.checkbox("Trứng (15K)")
col_1, col_2 = st.columns(2)
with col_1:
    topping = st.multiselect("Topping", ["Trân châu trắng (5K)", "Trân châu đen (5K)", "Thạch rau câu (6K)", "Vải (7K)", "Nhãn (8K)", "Đào (10K)"])
with col_2:
    num = int(st.number_input("Số lượng"))
note = st.text_area("Ghi chú")
if st.button("Đặt hàng", use_container_width=True):
    if size == "Nhỏ (30K)":
        price = 30
        size_n = "Cỡ nhỏ"
    elif size == "Vừa (40K)":
        price = 40
        size_n = "Cỡ vừa"
    else:
        price = 50
        size_n = "Cỡ lớn"

    addition = []
    add_price = [5, 8, 10, 15]
    add_total = 0
    if add_1:
        add_total += 5
        addition.append("Sữa")
    if add_2:
        add_total += 8
        addition.append("Cà phê")
    if add_3:
        add_total += 10
        addition.append("Kem")
    if add_4:
        add_total += 15
        addition.append("Trứng")

    dic_topping = {"Trân châu trắng (5K)" : 5, "Trân châu đen (5K)" : 5, "Thạch rau câu (6K)" : 6, "Vải (7K)" : 7, "Nhãn (8K)" : 8, "Đào (10K)" : 10}
    b = []
    for i in range(len(topping)):
        if topping[i] in dic_topping.keys():
            b.append(dic_topping[topping[i]])
    topping_total = sum(b)

    total = (price + add_total + topping_total) * num

    addition = ", ".join(str(e) for e in addition)
    topping = ", ".join(str(j) for j in topping)

    st.success(f"""
    {size_n}\n
    Thêm: {addition}\n
    Topping: {topping}\n
    {note}\n
    Số lượng: {str(num)}\n
    Thành tiền: {str(total)}K\n
    """)








