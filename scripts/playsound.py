package voiceLanucher;

import java.io.File;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;


public class playSound {
	
	String path ="/Users/ankiegao/Desktop/audio/"; 
	String animal = "";
	String suffix = ".wav";
	
	public void sound() {
		
		File sound = new File(path+animal+suffix);
		PlaySound(sound);
	}

	private static void PlaySound(File Sound) {
		try {
			Clip clip = AudioSystem.getClip();
			clip.open(AudioSystem.getAudioInputStream(Sound));
			clip.start();
			
			Thread.sleep(clip.getMicrosecondLength()/1000);
		
		}catch(Exception e) {
			System.err.println("Problem when playing sound : " + e);
		}
	}
}
