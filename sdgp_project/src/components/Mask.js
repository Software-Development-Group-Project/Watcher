import React, { Component } from 'react';

import '../CSS/mask.css'
import Webcam from "react-webcam";

class Mask extends Component {
    render() { 
        
        const videoConstraints = {
            width: 640,
            height: 360,
            facingMode: "user"
          };

        
        return ( 
                <div className="container" id="fea">
                    <Webcam
                        audio={false}
                        height={360}
                        // ref={webcamRef}
                        screenshotFormat="image/jpeg"
                        width={640}
                        videoConstraints={videoConstraints}
                    />
                     
                </div>
        );
          
          
        
 
    }
}

 
export default Mask;