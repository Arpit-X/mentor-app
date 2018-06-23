import React, { Component } from 'react'

class InputEx extends Component{
    state={name="",pass=""}

    saveName =(event) =>{
        const { target:{value}} = event;
        this.setState({
            name:value
        });
    }

    savePass = (event)=>{
        const { target:{value}} = event;
        this.setState({
            name:value
        });
    }
    submit = (event) =>{
        const {name,pass} = this.state;
        fetch('')
        .then(res => res.json())
        .then(response =>{ console.log('response',response) })
    }
    render
}