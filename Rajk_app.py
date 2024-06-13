import streamlit as st
from data_streamlit import names, match_percentages
from data2_v2_streamlit import top_5_matches

def rajk():
    st.title("Rajkos matchmaker")

    # 1. funkció: két ember közötti match százalék
    st.header("Párok")

    # két legördülő lista - nevek ABC sorrendbe rendezve
    f1_list_names1 = st.selectbox("Válassz egy nevet:", sorted(names))
    f1_list_names2 = st.selectbox("Válassz egy másik nevet:", sorted(names))

    # gomb + parancs
    if st.button("Mehet"):
        if (f1_list_names1, f1_list_names2) in match_percentages:
            percentage = match_percentages[(f1_list_names1, f1_list_names2)]
            formatted_percentage = f"{round(percentage * 100, 2):.2f}%" # eredmény formázása
            st.success(f"{formatted_percentage}")
        else:
            st.warning("Nincs adat ehhez a párhoz.")

    # 2. funkció: A hozzád legjobban passzoló 5 kollégista
    st.header("A hozzád legjobban passzoló 5 kollégista")

    # nevek - ABC sorrendbe rendezve
    f2_list_names = st.selectbox("Válassz egy személyt:", sorted(top_5_matches.keys()))

    # Milyen kapcsolatot keresel? 
    st.subheader("Milyen kapcsolatot keresel?")

    # Hetero, Meleg és Mindkettőre nyitott vagyok opciók gombokkal
    relationship_type = st.radio("Válaszd ki a kapcsolat típusát:", ("Hetero", "Meleg", "Mindkettőre nyitott vagyok"))

    # gomb + parancs
    if st.button("Mehet", key="mehet2"):
        if f2_list_names in top_5_matches:
            top_matches = []

            if relationship_type == "Hetero":
                top_matches.extend(top_5_matches[f2_list_names]["hetero"])
            elif relationship_type == "Meleg":
                top_matches.extend(top_5_matches[f2_list_names]["meleg"])
            elif relationship_type == "Mindkettőre nyitott vagyok":
                top_matches.extend(top_5_matches[f2_list_names]["all"])

            # top 5 kiválasztása
            top_matches_sorted = sorted(top_matches, key=lambda x: x[1], reverse=True)
            top_5_final_matches = top_matches_sorted[:5]

            if top_5_final_matches:
                st.success("Top 5:")
                for name, match_percent, hetero_meleg in top_5_final_matches:
                    formatted_percentage = f"{round(match_percent * 100, 2):.2f}%" # eredmény formázása
                    st.write(f"{name}: {formatted_percentage}")
            else:
                st.warning("Nincs megfelelő adat ehhez a kapcsolat típushoz.")
        else:
            st.warning("Nincs adat ehhez a személyhez.")

if __name__ == "__main__":
    rajk()
