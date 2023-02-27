import numpy as np
import pandas as pd
import streamlit as st
import pickle
import streamlit.components.v1 as stc

custom_title = """
<div style="font-size:40px;font-weight:bolder;background-color:#fff;padding:30px;
border-radius:20px;border:10px solid #464e5f;text-align:center;">
		<span style='color:blue'>M</span>
		<span style='color:black'>E</span>
		<span style='color:red'>D</span>
		<span style='color:green'>I</span>
		<span style='color:purple'>C</span>
		<span style='color:blue'>A</span>
		<span style='color:red'>L</span>
        &nbsp;
		<span style='color:yellow'>I</span>
		<span style='color:#464e5f'>N</span>
		<span style='color:red'>S</span>
		<span style='color:green'>U</span>
		<span style='color:yellow'>R</span>
		<span style='color:black'>A</span>
		<span style='color:blue'>N</span>
        <span style='color:#464e5f'>C</span>
        <span style='color:purple'>E</span>
</div>
"""


#st.title("Insurance Premium Prediction")
model = pickle.load(open('saved_models/0/model/model.pkl', 'rb'))
encoder = pickle.load(open('saved_models/0/target_encoder/target_encoder.pkl', 'rb'))
transformer = pickle.load(open('saved_models/0/transformer/transformer.pkl', 'rb'))

def main():

    stc.html(custom_title)
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        age = st.text_input('Enter Age', 18)
        age = int(age)

        sex = st.selectbox(
            'Please select gender',
            ('male', 'female'))
        # gender = encoder.transform(np.array([sex]))

        bmi = st.text_input('Enter BMI', 18)
        bmi = float(bmi)

        children = st.selectbox(
            'Please select number of children ',
            (0,1,2,3,4,5))
        children = int(children)


        smoker = st.selectbox(
            'Please select smoker category ',
            ("yes","no"))
        # smoker = encoder.transform(smoker)

        region = st.selectbox(
            'Please select region ',
            ("southwest", "southeast", "northeast", "northwest"))


        l = {}
        l['age'] = age
        l['sex'] = sex
        l['bmi'] = bmi
        l['children'] = children
        l['smoker'] = smoker
        l['region'] = region

        df = pd.DataFrame(l, index=[0])

        df['region'] = encoder.transform(df['region'])
        df['sex'] = df['sex'].map({'male':1, 'female':0})
        df['smoker'] = df['smoker'].map({'yes':1, 'no':0})

        df = transformer.transform(df)
        # dtrain = xg.DMatrix(df)
        y_pred = model.predict(df)
        # st.write(age, gender, bmi, children, smoker, region)
        with st.expander("Your Selected Options"):
            result = {
                "Age": age,
                "Sex": sex,
                "BMI": bmi,
                "Smoke": smoker,
                "Region": region,
                "Children": children,
            }
            st.write(result)

        if st.button("Show Result"):
            # col1,col2, col3,col4 = st.columns(4)
            st.success(f'''
            Thank you for your response!
            The Insurance Premium will be : {round(y_pred[0],2)} INR ''')
    else:
        st.header("About")

        st.image("extra/insurance.jpg", use_column_width=True)
        st.markdown(
            """
        # What is Insurance?
        Insurance is a legal agreement between two parties i.e. the insurance company (insurer) and the individual (insured). In this, the insurance company promises to make good the losses of the insured on happening of the insured contingency. The contingency is the event which causes a loss. It can be the death of the policyholder or damage/destruction of the property. It’s called a contingency because there’s an uncertainty regarding happening of the event. The insured pays a premium in return for the promise made by the insurer.  
        """
        )

        st.markdown(
            """
        ## How does insurance work?
        The insurer and the insured get a legal contract for the insurance, which is called the insurance policy. The insurance policy has details about the conditions and circumstances under which the insurance company will pay out the insurance amount to either the insured person or the nominees. Insurance is a way of protecting yourself and your family from a financial loss. Generally, the premium for a big insurance cover is much lesser in terms of money paid. The insurance company takes this risk of providing a high cover for a small premium because very few insured people actually end up claiming the insurance. This is why you get insurance for a big amount at a low price. Any individual or company can seek insurance from an insurance company, but the decision to provide insurance is at the discretion of the insurance company. The insurance company will evaluate the claim application to make a decision. Generally, insurance companies refuse to provide insurance to high-risk applicants.  
        """
        )
        st.image("extra/insurance_work.png", use_column_width=True)

        st.markdown(
            """
        ## What are the types of insurance available in India?
        """
        )

        st.markdown(
            """
        ### Life insurance
        As the name suggests, life insurance is insurance on your life. You buy life insurance to make sure your dependents are financially secured in the event of your untimely demise. Life insurance is particularly important if you are the sole breadwinner for your family or if your family is heavily reliant on your income. Under life insurance, the policyholder’s family is financially compensated in case the policyholder expires during the term of the policy.  
        """
        )
        st.image("extra/life_insurance_gif.gif", use_column_width=True)
        st.markdown(
            """
        ### Health insurance or Medical Insurance
        #### We will be focus on Medical Insurance
        Health insurance is bought to cover medical costs for expensive treatments. Different types of health insurance policies cover an array of diseases and ailments. You can buy a generic health insurance policy as well as policies for specific diseases. The premium paid towards a health insurance policy usually covers treatment, hospitalization and medication costs.  
        """
        )
        st.image("extra/health_insurance.gif", use_column_width=True)
        st.markdown(
            """
        ### Car insurance
        In today’s world, a car insurance is an important policy for every car owner. This insurance protects you against any untoward incident like accidents. Some policies also compensate for damages to your car during natural calamities like floods or earthquakes. It also covers third-party liability where you have to pay damages to other vehicle owners.  
        """
        )
        st.image("extra/car_insurance.gif", use_column_width=True)
        st.markdown(
            """
        ### Education Insurance
        The child education insurance is akin to a life insurance policy which has been specially designed as a saving tool. An education insurance can be a great way to provide a lump sum amount of money when your child reaches the age for higher education and gains entry into college (18 years and above). This fund can then be used to pay for your child’s higher education expenses. Under this insurance, the child is the life assured or the recipient of the funds, while the parent/legal guardian is the owner of the policy. You can estimate the amount of money that will go into funding your children’s higher education using Education Planning Calculator.  
        """
        )
        st.image("extra/education.gif", use_column_width=True)
        st.markdown(
            """
        ### Home insurance
        We all dreaming of owning our own homes. Home insurance can help with covering loss or damage caused to your home due to accidents like fire and other natural calamities or perils. Home insurance covers other instances like lightning, earthquakes etc.  
        """
        )
        st.image("extra/Money_Homeowners_insurance.gif", use_column_width=True)
        st.markdown(
            """
        ## What are the tax benefits on insurance?
        Apart from the safety and security benefits of buying insurance, there are also the income tax benefits that you can avail.
        Life insurance premium of up to ₹1.5 lakh can be claimed as a tax-saving deduction under Section 80C
        Medical insurance premium of up to ₹25,000 for yourself and your family and ₹25,000 for your parents can be claimed as a tax-saving deduction under Section 80D
        """
        )

if __name__ == "__main__":
    main()