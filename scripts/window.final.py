package voiceLanucher;

import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.awt.LayoutManager;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.OverlayLayout;

public class window {
	public String test = "";
	private JPanel panel1 = new JPanel();
	private JPanel panel2 = new JPanel();
	private JPanel panel3 = new JPanel();
	private JPanel panel4 = new JPanel();
	private JPanel panel5 = new JPanel();
	private JPanel panel6 = new JPanel();
	private JFrame f;
	private JLabel label2;
	private JLabel label3;
	private JLabel label4;
	private JLabel label5;
	private JLabel label6;
	private JButton bt = new JButton("Start");
	private ImageIcon imageIcon;
	private Image image;
	private Image newimg;
	private JLabel picLabel;
	
	public void mainContent() throws IOException {
		//window
		f = new JFrame("How Animal Talks");
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
		f.setSize(590,300);
		f.setLocation(500,500);
		
		//button(p1 -> p2)
        ActionListener Action = new ActionListener() {
    		public void actionPerformed(ActionEvent e) {
    			changePanel1();
    			if (e.getSource() == bt){
    			    test = "pressed";
    			}
    		}
    	};
    	
    	panel1.setLayout(null);
    	bt.setBounds(250,120,90,60);
		panel1.add(bt);
		bt.addActionListener(Action);
		
		//p1
		panel1.setBackground(Color.white);
		
        //show panel1
		f.getContentPane().add(panel1);
		f.setVisible(true);
	}
		
	public void panelContent() throws IOException {
		
		//panel2-text & image for all panels
		LayoutManager overlay2 = new OverlayLayout(panel2);
		panel2.setLayout(overlay2);
		
		label2 = new JLabel("Loading...");
        label2.setFont(new Font("Serif", Font.BOLD, 22));
        label2.setForeground(Color.white);
        panel2.add(label2);
		
        imageIcon = new ImageIcon("pic.jpg");
        image = imageIcon.getImage();
        newimg = image.getScaledInstance(590, 300,  java.awt.Image.SCALE_SMOOTH);
        picLabel = new JLabel(new ImageIcon(newimg));
        panel2.add(picLabel);
        
        //panel3-text
		LayoutManager overlay3 = new OverlayLayout(panel3);
		panel3.setLayout(overlay3);
		
		label3 = new JLabel("Speaking...");
        label3.setFont(new Font("Serif", Font.BOLD, 22));
        label3.setForeground(Color.white);
		
        //panel4-text
		LayoutManager overlay4 = new OverlayLayout(panel4);
		panel4.setLayout(overlay4);
		
		label4 = new JLabel("Recognizing...");
        label4.setFont(new Font("Serif", Font.BOLD, 22));
        label4.setForeground(Color.white);
        
        //panel5-text
		LayoutManager overlay5 = new OverlayLayout(panel5);
		panel5.setLayout(overlay5);
		
		label5 = new JLabel("Playing sound...");
        label5.setFont(new Font("Serif", Font.BOLD, 22));
        label5.setForeground(Color.white);
        
        //panel6-text
		LayoutManager overlay6 = new OverlayLayout(panel6);
		panel6.setLayout(overlay6);
		
		label6 = new JLabel("Try again...");
        label6.setFont(new Font("Serif", Font.BOLD, 22));
        label6.setForeground(Color.white);
	}
	
	
	public void changePanel1() {
		f.getContentPane().remove(panel1);
		f.getContentPane().add(panel2);
		f.validate();
	}
	public void changePanel2() {
	    panel3.add(label3);
	    panel3.add(picLabel);
		f.getContentPane().remove(panel2);
		f.getContentPane().add(panel3);
		f.validate();
	}
	public void changePanel3() {
		panel4.add(label4);
        panel4.add(picLabel);
		f.getContentPane().removeAll();
		f.getContentPane().add(panel4);
		f.validate();
	}
	public void changePanel4() {
		panel5.add(label5);
        panel5.add(picLabel);
		f.getContentPane().removeAll();
		f.getContentPane().add(panel5);
		f.validate();
	}
	public void changePanel5() {
		panel6.add(label6);
        panel6.add(picLabel);
		f.getContentPane().removeAll();
		f.getContentPane().add(panel6);
		f.validate();
	}
}
