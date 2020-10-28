package voiceLanucher;

import java.io.IOException;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.util.props.PropertyException;

public class VoiceMain {

	public static void main(String[] args) throws IOException {
		window w = new window();
		playSound p = new playSound();
		
		String outcome;
		String[] namelist = {"bird","buffalo","bat","bear","chicken","cat","kitten","cow","cricket","crocodile","coyote","camel","Cheetah","dolphin","donkey","duck","dog","elephant","fly","frog","goat","horse","hyena","koala","jaguar","lion","monkey","owl","panther","peacock","pig","seal","sheep","snake","whale","wolf"};

		w.mainContent();
		w.panelContent();
		
		//press start button to launch
		while(w.test == "") {
			System.out.println("press to start");
		}
		    if (w.test == "pressed"){

		         try {
	                  // Configuration Object
			          System.out.println("loading...");
	                  Configuration configuration = new Configuration();
	                  configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
	                  configuration.setLanguageModelPath("5206.lm");
	                  configuration.setDictionaryPath("5206.dic");
	          
	                  LiveSpeechRecognizer recognize = new LiveSpeechRecognizer(configuration);
	                  recognize.startRecognition(true);
	                  System.out.println("loading complete!");
	          
	                  w.changePanel2(); //panel3=speaking
	                  SpeechResult result;
	                  
	                  while ((result = recognize.getResult()) != null) {
	                	  w.panelContent();
	        	  
	                     //Get recognized speech
	                      String word = result.getHypothesis();
	                      word = word.toLowerCase();
	        	          System.out.println(word);
	   	  
	        	          if(checkWord(namelist, word)==true) {
	        		          outcome = word;
	        		          System.out.println("GOT THE WORD");
	        		          w.changePanel4(); //panel5=playing sound
	        		  
	        		          p.animal = outcome; //play sound
	        		          p.sound();
	        		  
	        	          }else if (checkWord(namelist, word)==false) {
	            	          outcome = null;
	            	          System.out.println("NO SUCH WORD");
	            	          
	            	      w.changePanel5(); //panel6=try again
	        
	        	          }
	                  } 
	            } catch (IOException e) {
	                  System.err.println("Problem when loading : " + e);
	                  e.printStackTrace();
	            } catch (PropertyException e) {
	                  System.err.println("Problem configuring : " + e);            e.printStackTrace();
	            } 
	            }
	        }
	  public static boolean checkWord(String[] namelist, String value) {
			for (int n = 0; n < namelist.length; n++) {
				if (value.contentEquals(namelist[n])) {
					return true;
				}
			}
			return false;
	}

}
