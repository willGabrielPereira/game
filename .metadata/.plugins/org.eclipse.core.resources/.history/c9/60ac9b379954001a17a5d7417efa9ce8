package threadChat;

import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;

public class InputListener extends Thread{
	private ObjectInputStream input;
	private String message;
	
	public InputListener(InputStream stream) throws IOException {
		input = new ObjectInputStream(stream);
		message = "";
		start();
	}
	
	public void close() {
		//pass
	}
	
	public void run() {
		try {
			while(!message.equals("exit")){
				message = input.readUTF();
				System.out.println(message);
			}
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}
