import React, {Component} from 'react';
import { Link } from "react-router-dom";
//import CollegeDetail from "./collegeDetail";

class CollegeList extends Component{
    constructor(props){
            super(props)
            this.state={
                data:null
            }
    }
    componentDidMount(){
        fetch("http://127.0.0.1:8000/api/colleges/",
        {
            headers:{
                'Authorization':'Basic '+this.props.token
            }
        })
            .then(result => {return result.json()})
            .then((data)=>this.setState({Collegelist:data}))
    }
    render(){
        
        return (
            
                // <Router>
                <div>
                    
                {
                    this.state.Collegelist &&
                    this.state.Collegelist.map((collegeObj,index)=>(
                    <p key={index}>
                    <Link to={`/college/${collegeObj.id}`}>
                    {collegeObj.name}
                    </Link>
                    </p>
                    ))
                }
            {/* <Route path="colleges/:id" component={CollegeDetail}/> */}
                </div>
                
                // </Router>
            
        )
    }
}

export default CollegeList;