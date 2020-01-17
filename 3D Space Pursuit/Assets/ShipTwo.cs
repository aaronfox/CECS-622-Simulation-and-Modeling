using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShipTwo : MonoBehaviour
{
    public Transform otherShip; // The other ship's position, angle, and speed
    public Rigidbody rb;
    [Range(1.0f, 100.0f)]
    public float speed = 50.0f;
    public float alphaAngle = 30.0f;
    public float betaDistance = 10.0f;
    public Rigidbody otherShipRB;
    [Range(0.0f, 10.0f)]
    public float aggressionLevel = 7.0f;
    public GameObject otherShipGameObject;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();

        // Maintain constant velocity in forward direction
        rb.velocity = new Vector3(0, 0, speed);
        Random.InitState(43);
        StartCoroutine("Movements");
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

        float distance = Mathf.Abs(Vector3.Distance(otherShip.position, transform.position));

        float errorTolerance = 5.0f;

        Debug.Log("Ship Two Angle: " + angle + "\nShip Two Distance: " + distance);

        //float testingErrorTolerance = 10.0f;
        //if (angle < alphaAngle + testingErrorTolerance && angle > alphaAngle - testingErrorTolerance)
        //{
        //    Debug.Log("Ship Two: Within Angle distance of " + testingErrorTolerance+ "!");
        //    if (distance < betaDistance + testingErrorTolerance && distance > betaDistance - testingErrorTolerance)
        //    {
        //        Debug.Log("Ship Two: Within distance distance of " + testingErrorTolerance + "!");


        //        //Destroy(otherShipGameObject);
        //    }
        //}
        if (angle < alphaAngle + errorTolerance && angle > alphaAngle - errorTolerance)
        {
            if (distance < betaDistance + errorTolerance && distance > betaDistance - errorTolerance)
            {
                Debug.Log("Destroyed Ship One!");
                Destroy(otherShipGameObject);
                // Disable script at this point. The simulation is finished
                this.enabled = false;
                // Disable other script as well to prevent errors
                otherShipGameObject.GetComponent<ShipOne>().enabled = false;
            }
        }
        //Debug.Log("Angle == " + angle);
        //if (angle < 5.0f)
        //    print("close");

        
        //StartCoroutine("EscapeAwayFrom", 4.5f);
        //StartCoroutine("GoToward", 4.5f);

        // Adjust velocity to always aim from front of ship
        rb.velocity = transform.forward * speed;
    }

    IEnumerator Movements()
    {
        while (true)
        {
            yield return new WaitForSeconds(Random.Range(1, 3));
            if (Random.Range(0, 10) > aggressionLevel)
            {

                    //Debug.Log("Ship Two: Escaping away from");
                    EscapeAwayFrom(0.0f);
            }
            else
            {
                    //Debug.Log("Ship Two: Going toward");
                    GoToward(0.0f);
            }
        }
        
    }
    public void EscapeAwayFrom(float timeToWait)
    {
        float timeForPredictedPath = 50.0f;

        // Get predicted path of other ship 5 seconds from now
        Vector3 expectedOtherShipPosition = otherShipRB.position + otherShipRB.velocity * timeForPredictedPath * Time.deltaTime;

        // ROTATE AWAY FROM CODE
        // Determine which direction to rotate towarsds
        Vector3 targetDirection = transform.position - expectedOtherShipPosition;

        // The step size is equal to speed times frame time.
        float singleStep = speed * Time.deltaTime;

        // Rotate the forward vector towards the target direction by one step
        Vector3 newDirection = Vector3.RotateTowards(transform.forward, targetDirection, singleStep, 0.0f);

        // Draw a ray pointing at our target in
        Debug.DrawRay(transform.position, expectedOtherShipPosition - transform.position, Color.blue);//, 1.0f);

        // Calculate a rotation a step closer to the target and applies rotation to this object
        transform.rotation = Quaternion.LookRotation(newDirection);

        // END ROTATE AWAY FROM CODE
    }

    public void GoToward(float timeToWait)
    {

        // Use timeForPredictedPath to allow ship to take the allotted required time to get within
        // a beta distance of the other ship
        // NOTE: otherShipRB.velocity.magnitude is the magnitude of the speed of the other ship
        // Time needed is distance over time or m / m / s = s
        float timeForPredictedPath = betaDistance / otherShipRB.velocity.magnitude * 60;
        Debug.Log("timeForPredictedPath == " + timeForPredictedPath);

        // Get predicted path of other ship timeForPredictedPath seconds from now
        Vector3 expectedOtherShipPosition = otherShipRB.position + otherShipRB.velocity * timeForPredictedPath * Time.deltaTime;
        //Vector3 expectedOtherShipPosition = new Vector3(otherShipRB.position.x + otherShipRB.velocity.magnitude * timeForPredictedPath * Time.deltaTime, otherShipRB.position.y + otherShipRB.velocity.magnitude * timeForPredictedPath * Time.deltaTime, otherShipRB.position.z + otherShipRB.velocity.magnitude * timeForPredictedPath * Time.deltaTime);// + /*otherShipRB.velocity* */ + timeForPredictedPath * Time.deltaTime;

        // ROTATE TOWARD CODE
        // Determine which direction to rotate towards
        Vector3 targetDirection = expectedOtherShipPosition - transform.position;

        // The step size is equal to speed times frame time.
        float singleStep = speed * Time.deltaTime;

        // Rotate the forward vector towards the target direction by one step
        Vector3 newDirection = Vector3.RotateTowards(transform.forward, targetDirection, singleStep, 0.0f); // TODO: see if alphaAngle should go here or not

        // Draw a ray pointing at our target's expected future direction
        Debug.DrawRay(transform.position, expectedOtherShipPosition - transform.position, Color.blue, 10.0f);

        // Calculate a rotation a step closer to the target and applies rotation to this object
        transform.rotation = Quaternion.LookRotation(newDirection);

        // Attempt to rotate to alpha angle specified to destroy ship
        //transform.Rotate(90.0f, 0.0f, 0.0f, Space.Self);

        // END ROTATE TOWARD CODE
    }
}