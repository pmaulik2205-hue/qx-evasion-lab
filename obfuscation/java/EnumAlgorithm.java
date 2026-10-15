// R4-05 Algorithm names held in an enum and used through a constant.
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;

public class EnumAlgorithm {
    enum SigAlg {
        LEGACY("RSA", "SHA256withRSA"),
        CURVE("EC", "SHA256withECDSA");

        final String keyAlg;
        final String jcaName;

        SigAlg(String keyAlg, String jcaName) { this.keyAlg = keyAlg; this.jcaName = jcaName; }
    }

    static final SigAlg ACTIVE = SigAlg.LEGACY;

    public static byte[] sign(byte[] data) throws Exception {
        KeyPair kp = KeyPairGenerator.getInstance(ACTIVE.keyAlg).generateKeyPair();
        Signature s = Signature.getInstance(ACTIVE.jcaName);
        s.initSign(kp.getPrivate());
        s.update(data);
        return s.sign();
    }
}
