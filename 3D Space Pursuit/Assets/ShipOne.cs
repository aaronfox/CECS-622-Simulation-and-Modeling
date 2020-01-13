using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShipOne : MonoBehaviour
{
    public Transform otherShip; // The other ship's position, angle, and speed
    public Rigidbody rb;
    public float speed = 60.0f;
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
