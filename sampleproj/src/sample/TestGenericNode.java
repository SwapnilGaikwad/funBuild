package sample;

import com.oracle.truffle.api.frame.VirtualFrame;
import com.oracle.truffle.api.nodes.Node;

public abstract class TestGenericNode extends Node {

	public abstract Object executeVoid(VirtualFrame frame);
	
}
