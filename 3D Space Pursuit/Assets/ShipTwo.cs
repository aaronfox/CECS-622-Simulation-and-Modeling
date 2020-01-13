using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShipTwo : MonoBehaviour
{
    public Transform otherShip; // The other ship's position, angle, and speed
    public Rigidbody rb;
    public float speed = 50.0f;
    public float alphaAngle = 30.0f;
    public float betaDistance = 10.0f;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();

        // Maintain constant velocity in forward direction
        rb.velocity = new Vector3(0, 0, speed);
    }

    // Update is called once per frame
    void Update()
    {

    }

    // Use this function for physics within Unity
    private void FixedUpdate()
    {
        Vector3 targetDir = otherShip.position - transform.position;
        float angle = Vector3.Angle(targetDir, transform.forward);
        Debug.Log("Angle == " + angle);
        //if (angle < 5.0f)
        //    print("close");
    }
}


//using System.Collections;
//using System.Collections.Generic;
//using UnityEngine;

//public class Escaper : MonoBehaviour
//{
//    // Get position of chaser to escape from
//    public Transform otherShip;
//    public Rigidbody rb;
//    public float speed = 50.0f;
//    // Start is called before the first frame update
//    void Start()
//    {
//        rb = GetComponent<Rigidbody>();

//        // Maintain constant velocity in forward direction
//        rb.velocity = new Vector3(0, 0, speed);
//    }

//    // Update is called once per frame
//    void Update()
//    {

//    }

//    private void FixedUpdate()
//    {
//        // Go at 90 angle away from chaser
//        //transform.Translate()

//        // Get chaser's angle
//        Vector3 chaserAngles = otherShip.rotation.eulerAngles;
//        Debug.Log("ChaserAngle = " + chaserAngles.ToString());
//        Debug.Log("Escaper Angle = " + transform.eulerAngles.ToString());

//        // Change Escaper's angle to be opposite of Chaser's angle
//        //float x = transform.rotation.eulerAngles.y;
//        transform.eulerAngles = new Vector3(chaserAngles.x + 180, chaserAngles.y + 180, transform.eulerAngles.z + 180);

//        //transform.Rotate()
//    }
//}
