import React, { Component } from 'react';
import img from '../images/mask.png';
import '../CSS/mask.css'
import Webcam from "react-webcam";

class Mask extends Component {
    render() { 
        
        

    const WebcamComponent = () => <Webcam />;
    
        return ( 
                <div>
                    <img src = {img} alt="alert"/> 
                    <p> Check People</p>
                    <p>This web cam can check whether you're wearing mask or not</p>
                    <WebcamComponent/>
                </div>
        );
 
    }
}
 
export default Mask;