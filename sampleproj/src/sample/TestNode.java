package sample;

import com.oracle.truffle.api.dsl.NodeChild;
import com.oracle.truffle.api.dsl.Specialization;
import com.oracle.truffle.api.frame.VirtualFrame;

@NodeChild(value="someValue")
public abstract class TestNode extends TestGenericNode {

	@Specialization
	public int printValue(VirtualFrame frame, int someValue){
		System.out.println("Some int value: " + someValue);
		return someValue;
	}
}
