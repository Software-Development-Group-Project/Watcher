import React, { Component } from 'react';
import img from '../images/alert.png'

class Alert extends Component {
    
    render() { 
        const styles = {
            width: "300px",
            margin: "auto",
            fontSize: "15px",
             
        } 

        return ( 
            <div style = {styles}>
                <img src = {img} alt="alert"/> 
                <p><b> Alert the User </b></p>
                <p style = {{textAlign: "justify"}}>the system detect people who are not
                 wear mask and it will alert the admin</p>
            </div>
         );
    }
}
 
export default Alert; 