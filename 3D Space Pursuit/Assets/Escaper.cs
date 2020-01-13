using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Escaper : MonoBehaviour
{
    // Get position of chaser to escape from
    public Transform chaser;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void FixedUpdate()
    {
        // Go at 90 angle away from chaser
        //transform.Translate()

        // Get chaser's angle
        Vector3 chaserAngles = chaser.rotation.eulerAngles;
        Debug.Log("ChaserAngle = " + chaserAngles.ToString());

        // Change Escaper's angle to be opposite of Chaser's angle
        float x = transform.rotation.eulerAngles.y;
        //transform.Rotate()
    }
}
