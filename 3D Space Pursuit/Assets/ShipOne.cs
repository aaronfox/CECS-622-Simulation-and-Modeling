using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShipOne : MonoBehaviour
{
    //public Transform otherShip; // The other ship's position, angle, and speed
    public Rigidbody otherShipRB;
    public Rigidbody rb;
    public float speed = 10.0f;
    public float alphaAngle = 30.0f;
    public float betaDistance = 10.0f;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();

        // Maintain constant velocity in forward direction
        rb.velocity = transform.forward * speed;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    // Use this function for physics within Unity
    private void FixedUpdate()
    {
        Vector3 targetDir = otherShipRB.position - transform.position;
        float angle = Vector3.Angle(targetDir, transform.forward);
        Debug.Log("Ship One Angle == " + angle);

        float dist = Vector3.Distance(otherShipRB.position, transform.position);
        print("Ship One Distance to other ship: " + dist);

        //if (angle < 5.0f)
        //    print("close");

        float timeForPredictedPath = 5.0f;
        // Get predicted path of other ship 5 seconds from now
        Vector3 expectedOtherShipPosition = otherShipRB.position + otherShipRB.velocity * timeForPredictedPath * Time.deltaTime;
        Debug.Log("Ship One: expectedOtherShipPosition in " + timeForPredictedPath + " seconds: " + expectedOtherShipPosition.ToString());

        float step = speed * Time.deltaTime; // calculate distance to move
        Debug.Log("Ship One: Step == " + step);
        // Move ship toward other ship's predicted location
        transform.position = Vector3.MoveTowards(transform.position, otherShipRB.position, step);

        // ROTATE TOWARD CODE
        // Determine which direction to rotate towards
        Vector3 targetDirection = otherShipRB.position - transform.position;

        // The step size is equal to speed times frame time.
        float singleStep = speed * Time.deltaTime;

        // Rotate the forward vector towards the target direction by one step
        Vector3 newDirection = Vector3.RotateTowards(transform.forward, targetDirection, singleStep, 0.0f);

        // Draw a ray pointing at our target in
        Debug.DrawRay(transform.position, newDirection, Color.red);

        // Calculate a rotation a step closer to the target and applies rotation to this object
        transform.rotation = Quaternion.LookRotation(newDirection);


        // END ROTATE TOWARD CODE

        // Adjust velocity to always aim from front of ship
        rb.velocity = transform.forward * speed;



    }
}
