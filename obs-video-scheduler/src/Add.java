import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

import util.OBSApi;

public class Add {
	public static void main(String[] args) throws FileNotFoundException, IOException, InterruptedException {
		new OBSApi().launchVideo("all teams video.mp4");
	}
}