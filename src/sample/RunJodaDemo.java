package sample;

import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;

public class RunJodaDemo {

	public static void main(String[] args) {
		DateTime dt = new DateTime();
		System.out.println("Current Time: " + dt.toLocalTime() + " " + dt.getZone());
		dt =dt.toDateTime(DateTimeZone.forID("America/New_York"));
		System.out.println("New York Time: " + dt.toLocalTime() + " " + dt.getZone());
	}

}
