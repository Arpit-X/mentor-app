import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import  HeaderProp from './headerProp'
import CollegeList from "./collegeList"
import { BrowserRouter as Router,Route } from "react-router-dom";
import CollegeDetail from './collegeDetail';
class App extends Component {
 getToken =(username,password)=>{
      return btoa(`${username}:${password}`)   
 }
 testFun= ()=> { console.log("working")}
  render() {
    let  key = this.getToken("arpit","test1234")
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <HeaderProp title="The Crazy Blogger" username="Akhil"/>  
        </header>
        <Router>
          <div>
            <Route exact path="/" render={(props) => <CollegeList  token={key} {...props}/>}/>
            <Route exact path="/college/:id" render={(props)=> <CollegeDetail token={key} {...props}/>}/>
          </div>
        </Router>
      
        
        
      </div>
    );
  }
}

export default App;
