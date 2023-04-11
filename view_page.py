import streamlit as st


class Multiapp():
  def __init__(self):
    self.apps=[]
    
  def add_app(self,title,function):
    self.apps.append({'title':title,'func':function})
    
  def run(self):
    app = st.sidebar.selectbox('Navigation',self.apps,format_func = lambda app : app['title'])
    app['function']()
    