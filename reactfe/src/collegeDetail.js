import React , { Component } from 'react';

class CollegeDetail extends Component{
    constructor(props){
        
        super(props)
        this.state={
            studentList:null,
            collegeId:props.match.params.id
        }
    }
    componentDidMount(){
        fetch(`http://127.0.0.1:8000/api/colleges/${this.state.collegeId}/students/`,
        {
            headers:{
                'Authorization':'Basic '+this.props.token
            }
        })
        .then(result => result.json())
        .then((data) => {
            this.setState({studentList:data})
        })
    }
    render(){
        return (
            <center>
            <div className="details">
                <table className="table table-striped">
                    <thead>
                        <tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>DB Folder</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.studentList &&
                            this.state.studentList.map((studentObj,index)=>(
                                <tr key={index}>
                                    <td>{studentObj.id}</td>
                                    <td>{studentObj.name}</td>
                                    <td>{studentObj.email}</td>
                                    <td>{studentObj.db_folder}</td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
            </div>
            </center>
        )
    }
}
export default CollegeDetail;