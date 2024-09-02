import streamlit as st
import pandas as pd 
import random 
import plotly.graph_objects as go

@st.cache_data  
def load_data():
    df = pd.read_csv('bank.csv') 
    return df


try:
    df = load_data() 
except FileNotFoundError:
    st.error("Error: File not found.")
except pd.errors.ParserError:
    st.error("Error: Invalid data format.")
else:
    st.markdown("<h4> Customer Understanding </h'5'>", unsafe_allow_html=True)
    st.markdown("<h5> 1.What is the typical profile of the customer who takes out a term deposit? (age, profession, marital status, education level, etc.) </h5>", unsafe_allow_html=True)
    df_yes = df[df['deposit']=='yes']

    # job profile
    job_counts = df_yes['job'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(job_counts))]
    fig_job = go.Figure(data=[
        go.Bar(
            x=job_counts.index, 
            y=job_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_job.update_layout(
        title=" Job title for clients who takes out a term deposit ",
        xaxis_title="Job title",
        yaxis_title="Number of clients",
        template="plotly_white"
    )

    # marital status profile
    marital_counts = df_yes['marital'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(marital_counts))]
    fig_marital = go.Figure(data=[
        go.Bar(
            x=marital_counts.index, 
            y=marital_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_marital.update_layout(
        title="Marital Status for clients who takes out a term deposit",
        xaxis_title="marital",
        yaxis_title="Number of clients",
        template="plotly_white"
    )

    # education profile
    education_counts = df_yes['education'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(education_counts))]
    fig_education = go.Figure(data=[
        go.Bar(
            x=education_counts.index, 
            y=education_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_education.update_layout(
        title="Education Level for clients who takes out a term deposit",
        xaxis_title="Education level",
        yaxis_title="Number of clients",
        template="plotly_white"
    )

    # age profile
    bins = [0, 18, 30, 40, 50, 60, 100]
    labels = ['0-18', '18-30', '30-40', '40-50', '50-60', '60+']
    df['AgeGroup'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    data = df[df['deposit']=='yes']
    age_counts = data['AgeGroup'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(age_counts))]
    fig_age = go.Figure(data=[
        go.Bar(
            x=age_counts.index, 
            y=age_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_age.update_layout(
        title="Age Category for clients who takes out a term deposit",
        xaxis_title="Age group",
        yaxis_title="Number of clients",
        template="plotly_white"
    )

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_job)
        st.plotly_chart(fig_education)
    with col2:
        st.plotly_chart(fig_marital)
        st.plotly_chart(fig_age)
    st.markdown("<p style='text-align: center;'> The typical term deposit subscriber is a married individual between the ages of 30 and 40, holding a management position, and possessing a secondary education level. This demographic exhibits a higher propensity for subscribing to term deposits compared to other customer segments. </p>", unsafe_allow_html=True)

    st.markdown("<h5> 2.How do housing and personal loans impact the decision to subscribe? </h5>", unsafe_allow_html=True)
    housing_counts = df_yes['housing'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(housing_counts))]
    fig_housing = go.Figure(data=[
        go.Bar(
            x=housing_counts.index, 
            y=housing_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_housing.update_layout(
        title="Housing impact the decision to subscribe",
        xaxis_title="Housing",
        yaxis_title="Number of clients",
        template="plotly_white"
    )

    loan_counts = df_yes['loan'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(loan_counts))]
    fig_loan = go.Figure(data=[
        go.Bar(
            x=loan_counts.index, 
            y=loan_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_loan.update_layout(
        title="Personal loans impact the decision to subscribe",
        xaxis_title="loan",
        yaxis_title="Number of clients",
        template="plotly_white"
    )

    col3,col4 = st.columns(2)
    with col3 : 
        st.plotly_chart(fig_housing)
    with col4 : 
        st.plotly_chart(fig_loan)
    st.markdown("<p style='text-align: center;'> Term deposit subscribers are often characterized by the absence of both housing and personal loans. This suggests that individuals with fewer financial obligations might be more inclined towards securing a term deposit. This observation highlights the potential correlation between financial freedom and a propensity for term deposit subscriptions. </p>", unsafe_allow_html=True)


    st.markdown("<h5> 3.What is the impact of the duration of the last contact on the likelihood of subscribing? </h5>", unsafe_allow_html=True)
    bins = [0, 500, 1000, 1500, 2000, 3000, 3881]  
    labels = ['0-500', '500-1000', '1000-1500', '1500-2000', '2000-3000', '3000-3881']
    data['DurationGroup'] = pd.cut(df['duration'], bins=bins, labels=labels, right=False)
    DurationGroup_counts = data['DurationGroup'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(DurationGroup_counts))]
    fig_DurationGroup = go.Figure(data=[
        go.Bar(
            x=DurationGroup_counts.index, 
            y=DurationGroup_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_DurationGroup.update_layout(
        title="the impact of the duration of the last contact on the likelihood of subscribing",
        xaxis_title="Duration Group",
        yaxis_title="Number of clients",
        template="plotly_white"
    )
    st.plotly_chart(fig_DurationGroup)
    st.markdown("<p style='text-align: center;'> The typical client who takes out a term deposit is more likely to have a shorter last contact duration, less than 1000 seconds. </p>", unsafe_allow_html=True)


    st.markdown("<h5> 4.What is the best time of year to contact clients to maximize subscription rates? </h5>", unsafe_allow_html=True)
    month_counts = data['month'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(month_counts))]
    fig_month = go.Figure(data=[
        go.Bar(
            x=month_counts.index, 
            y=month_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_month.update_layout(
        title="the best time of year to contact clients to maximize subscription rates based on Month",
        xaxis_title="Month",
        yaxis_title="Number of clients",
        template="plotly_white"
    )
    
    day_counts = data['day'].value_counts()
    day_counts_df = pd.DataFrame({'day': day_counts.index, 'count': day_counts.values})
    day_counts_df = day_counts_df.sort_values('day')
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(day_counts_df['day'].unique()))]
    fig_day = go.Figure(data=[
        go.Bar(
            x=day_counts_df['day'], 
            y=day_counts_df['count'],
            marker=dict(color=colors)
        )
    ])
    fig_day.update_layout(
        title="the best time of year to contact clients to maximize subscription rates based on day",
        xaxis_title="Day of the month",
        yaxis_title="Number of clients",
        template="plotly_white"
    )
    
    col5,col6 = st.columns(2)
    with col5 : 
        st.plotly_chart(fig_month)
    with col6 : 
        st.plotly_chart(fig_day)
    st.markdown("<p style='text-align: center;'>The best time of year to contact clients to maximize subscription rates appears to be during the months of April, May, June, July, and August. Within these months, the most successful contact days tend to fall at the beginning, middle, and end of the month. </p>", unsafe_allow_html=True)


    # Marketing compaine
    st.markdown("<h4> Marketing Campaigns </h4>", unsafe_allow_html=True)
    st.markdown("<h5> 5.Which communication channel is most effective for contacting clients (cellular vs. phone)? </h5>", unsafe_allow_html=True)
    contact_counts = data['contact'].value_counts()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(contact_counts))]
    fig_contact = go.Figure(data=[
        go.Bar(
            x=contact_counts.index, 
            y=contact_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_contact.update_layout(
        title="Most communication channel effective for contacting clients (cellular vs. phone)",
        xaxis_title="Contact type",
        yaxis_title="Number of clients",
        template="plotly_white"
    )
    st.plotly_chart(fig_contact)
    st.markdown("<p style='text-align: center;'>The most effective communication channel for contacting clients appears to be cellular. This suggests that reaching clients directly on their mobile phones yields the highest success rate. </p>", unsafe_allow_html=True)


    st.markdown("<h5> 6.Are clients who have previously defaulted on credit more responsive to marketing campaigns? </h5>", unsafe_allow_html=True)
    default_counts = data['default'].value_counts().sort_values()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(default_counts))]
    fig_default = go.Figure(data=[
        go.Bar(
            x=default_counts.index, 
            y=default_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_default.update_layout(
        title="Impact of Defaults on Marketing Campaign Response",
        xaxis_title="Default",
        yaxis_title="Number of clients",
        template="plotly_white"
    )
    st.plotly_chart(fig_default)
    st.markdown("<p style='text-align: center;'>Clients who have not previously defaulted on credit appear to be more responsive to marketing campaigns. This suggests that a history of responsible financial behavior may make individuals more receptive to new financial products. </p>", unsafe_allow_html=True)


    st.markdown("<h5> 7.What is the impact of the number of contacts on the likelihood of subscribing? </h5>", unsafe_allow_html=True)
    campaign_counts = data['campaign'].value_counts().sort_values()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(campaign_counts))]
    fig_campaign = go.Figure(data=[
        go.Bar(
            x=campaign_counts.index, 
            y=campaign_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_campaign.update_layout(
        title="the impact of the number of contacts on the likelihood of subscribing",
        xaxis_title="Compaigne",
        yaxis_title="Number of clients",
        template="plotly_white"
    )
    st.plotly_chart(fig_campaign)
    st.markdown("<p style='text-align: center;'>Interestingly, clients who receive a lower number of contacts during a campaign are more likely to subscribe to a term deposit. This suggests that a more targeted and less persistent approach may be more effective in securing subscriptions. </p>", unsafe_allow_html=True)


    st.markdown("<h5> 8.What is the effectiveness of different marketing strategies (check, success, success)? </h5>", unsafe_allow_html=True)
    poutcome_counts = data['poutcome'].value_counts().sort_values()
    colors = [random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(poutcome_counts))]
    fig_poutcome = go.Figure(data=[
        go.Bar(
            x=poutcome_counts.index, 
            y=poutcome_counts.values,
            marker=dict(color=colors)
        )
    ])
    fig_poutcome.update_layout(
        title="the effectiveness of different marketing strategies (check, success, success",
        xaxis_title="Poutcome",
        yaxis_title="Number of clients",
        template="plotly_white"
    )
    st.plotly_chart(fig_poutcome)
    st.markdown("<p style='text-align: center;'>The last marketing campaign yielded only 1000 clients with a successful term deposit subscription. Data limitations prevent us from analyzing the results for over 3000 clients. This highlights the need for more complete data to fully assess the campaign's effectiveness. </p>", unsafe_allow_html=True)
