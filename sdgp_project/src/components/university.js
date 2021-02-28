import React, { Component } from 'react';
import img from '../images/uni.jpg'

class University extends Component {
     
    render() { 
        const styles = {
            width: "300px",
            margin: "auto",
            fontSize: "15px",
             
        } 
         
        return (
            <div style = {styles}>
                <h3>University</h3>
                <img src= { img } width = "300px" height = "250px" alt = "a university" />
                <p style = {{textAlign: "justify"}}>The Face Mask Detection System can be used at university to check students and staffs. 
                   Our system is best fit for the university’s because the management of university already 
                   have the data of the students and the staffs so If they do not wear a mask we can simply 
                   identify them and alert.Normally lot of people are connect with university daily so Security 
                   system like watcher will defiantly help the management to manage large amount of student</p> 
            </div>
        );
    }
}
 
export default University;