import React, { Component } from 'react';
import img from '../images/mask.png';
import '../CSS/mask.css'
import Webcam from "react-webcam";

class Mask extends Component {
    render() { 
        
        const videoConstraints = {
            width: 1280,
            height: 720,
            facingMode: "user"
          };

        
        return ( 
                <div>
                    <img src = {img} alt="alert"/> 
                    <p> Check People</p>
                    <p>This web cam can check whether you're wearing mask or not</p>
                    <Webcam
                        audio={false}
                        height={720}
                        // ref={webcamRef}
                        screenshotFormat="image/jpeg"
                        width={1280}
                        videoConstraints={videoConstraints}
                    />
                    <button >Capture photo</button>
                </div>
        );
          
          
        
 
    }
}

 
export default Mask;