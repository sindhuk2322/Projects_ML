import pickle
import streamlit as st
import pandas as pd


# Page config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="C:/Users/SVI/Desktop/Jupyter NB Codes/aiml_mini_project/images/icon.png",)

# Page title
st.title('Customer Churn Predictor')
st.image('C:/Users/SVI/Desktop/Jupyter NB Codes/aiml_mini_project/images/main_screen.png')
st.write("\n\n")

st.markdown(
    """
    This app aims to predict customers who are likely to churn in the future. Customer churn refers to the phenomenon where customers discontinue their services with a company, which can lead to revenue loss and decreased customer satisfaction. 
    """
)

# Load the model
with open('C:/Users/SVI/Desktop/Jupyter NB Codes/aiml_mini_project/model/gb_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit interface to input data
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(label='Type', options=['Female', 'Male'])
    senior_citizen = st.number_input(label='0: No or 1: Yes')
    tenure = st.number_input(label='Tenure in Months')
    contract = st.selectbox(label='Contract Type', options=[
                            'Month-to-month', 'One year', 'Two year'])
with col2:
    paperless_billing = st.selectbox(
        label='PaperlessBilling Type', options=['Yes', 'No'])
    payment_method = st.selectbox(label='Payment Type', options=[
                                  'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthly_charges = st.number_input(label='Monthly Charges')
    total_charges = st.number_input(label='Total Charges')

# Function to predict the input


def prediction(gender, senior_citizen, tenure, contract, paperless_billing, payment_method, monthly_charges, total_charges):
    # Create a df with input data
    df_input = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [senior_citizen],
        'tenure': [tenure],
        'Contract': [contract],
        'PaperlessBilling': [paperless_billing],
        'PaymentMethod': [payment_method],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
    })

    prediction = model.predict(df_input)
    return prediction


# Button to predict
if st.button('Predict'):
    predict = prediction(gender, senior_citizen, tenure, contract,
                         paperless_billing, payment_method, monthly_charges, total_charges)

    # Print result
    if predict[0] == 1:
        st.success("Churn, the customer is likely to churn.")

        # Display strategies for customer retention and win back churned customers
        st.subheader(
            "Strategies for Customer Retention and Win Back Churned Customers:")
        st.write("""
        Strategies for Customer Retention:

        - Personalized Offers: Offer personalized retention incentives, discounts, or loyalty rewards to long-term customers with higher total charges to encourage them to stay.
        - Onboarding Programs: Implement onboarding programs for new customers to help them understand the value of your services and foster a positive early experience.
        - Price Optimization: Consider pricing strategies to retain customers with lower total charges, such as offering more affordable plans or add-on services.
        - Customer Engagement: Continuously engage with customers through proactive communication and feedback surveys to address their needs and concerns.
        - Senior Citizen Benefits: Recognize and cater to the needs of senior citizens by providing specialized services or discounts, as they tend to have slightly higher total charges.
        
        Bringing Back Churned Customers:

        - Win-Back Campaigns: Launch targeted win-back campaigns to re-engage with churned customers. Offer enticing promotions or value-added services to entice them to return.
        - Customer Feedback: Gather feedback from churned customers to understand their reasons for leaving. Address these issues and communicate improvements.
        - Reactivation Offers: Create special reactivation offers for churned customers, providing them with incentives to rejoin your services.
        - Retargeting: Use digital marketing and retargeting strategies to reach out to churned customers and remind them of the benefits of your services.
        - Data Analysis: Continuously analyze churned customer data to identify patterns and reasons for churn. Use these insights to refine your retention strategies.
        """)
    else:
        st.success("Not Churn, the customer is not predicted to churn.")
