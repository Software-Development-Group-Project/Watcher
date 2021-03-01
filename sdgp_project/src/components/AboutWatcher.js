import React from 'react';
import '../CSS/aboutWatcher.css';
import {ReactComponent as CCTV} from '../images/cctv.svg';
import {ReactComponent as TV} from '../images/tv.svg';
import {ReactComponent as Mobile} from '../images/mobile-vibration.svg';

class About extends React.Component{
    render(){
        return (
            <div id="about-page">
                <h4>How watcher works?</h4>
                <div id="about-container">
                    <div class="about-info-container">  
                        <CCTV/>
                        <article>
                            <h5>Scanning People</h5>
                            <p>Scan people to identify whether all wearing mask or not by scanning their face whether they wear mask or not</p>
                        </article>
                    </div>
                    <div class="about-info-container">
                        <TV/>
                        <article>
                            <h5>Display Video</h5>
                            <p>Displaying live video stream that is scanned by cctv camera. And show people and their detaila if they didn't wear mask</p>
                        </article>
                    </div>
                    <div class="about-info-container">
                        <Mobile/>
                        <article>
                            <h5>Alert User</h5>
                            <p>If a person deteced without mask then watcher will alert them by sending them a message or email and admin</p>
                        </article>
                    </div>
                </div>
            </div>
        );
    }
}
export default About;