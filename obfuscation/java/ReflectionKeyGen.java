// R4-04 RSA key pair created through reflection; algorithm name built from pieces.
import java.lang.reflect.Method;
import java.security.KeyPair;

public class ReflectionKeyGen {
    public static void main(String[] args) throws Exception {
        Class<?> kpgClass = Class.forName("java.security." + "KeyPair" + "Generator");
        Method getInstance = kpgClass.getMethod("getInstance", String.class);
        Object kpg = getInstance.invoke(null, "R" + "S" + "A");
        kpgClass.getMethod("initialize", int.class).invoke(kpg, 2048);
        KeyPair kp = (KeyPair) kpgClass.getMethod("generateKeyPair").invoke(kpg);
        System.out.println(kp.getPublic().getAlgorithm());
    }
}
