import React from 'react';
import './about.css';
import {ReactComponent as CCTV} from '../../../assets/cctv.svg';
import {ReactComponent as TV} from '../../../assets/tv.svg';
import {ReactComponent as Mobile} from '../../../assets/mobile-vibration.svg';

class About extends React.Component{
    render(){
        return (
            <div id="about-page">
                <h2>How watcher works?</h2>
                <div id="about-container">
                    <div class="about-info-container">  
                        <CCTV/>
                        <article>
                            <h3>Scanning People</h3>
                            <p>Scan people to identify whether a person wearing mask or not</p>
                        </article>
                    </div>
                    <div class="about-info-container">
                        <TV/>
                        <article>
                            <h3>Display Video</h3>
                            <p>Displaying live video stream that is scanned my cctv camera. And show people and their detail if they didn't wear mask</p>
                        </article>
                    </div>
                    <div class="about-info-container">
                        <Mobile/>
                        <article>
                            <h3>Alert User</h3>
                            <p>If a person deteced that didn't wear mask the watcher will alert them by sending them a message</p>
                        </article>
                    </div>
                </div>
            </div>
        );
    }
}
export default About;