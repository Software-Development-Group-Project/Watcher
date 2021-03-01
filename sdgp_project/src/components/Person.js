import React, { Component } from 'react';
import img from '../images/person.png'

class Person extends Component {
    
    render() { 
        const styles = {
            width: "300px",
            margin: "auto",
            fontSize: "15px",
             
        } 

        return ( 
            <div style = {styles}>
                <img src = {img} alt="alert"/> 
                <p><b> Alert the Person </b></p>
                <p style = {{textAlign: "justify"}}>if the system can identify the person who is 
                not wear a mask then it can alert that person also</p>
            </div>
         );
    }
}
 
export default Person; 